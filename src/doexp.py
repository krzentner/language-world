#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import Union, List, Tuple
import os
import re
import subprocess
import psutil
import time
import shutil
import math
import sys


@dataclass(frozen=True)
class FileArg:
    filename: str


@dataclass(frozen=True)
class In(FileArg):
    pass


@dataclass(frozen=True)
class Out(FileArg):
    pass


@dataclass(frozen=True)
class Cmd:

    args: tuple
    extra_outputs: tuple
    extra_inputs: tuple
    warmup_time: float = 1.0
    ram_gb: float = 4.0
    priority: Union[int, Tuple[int, ...]] = 10
    gpus: Union[str, None] = None


_BYTES_PER_GB = (1024) ** 3
# If srun is installed, use slurm
_USING_SLURM = bool(shutil.which("srun"))
CUDA_DEVICES = []
next_cuda_device = 0


def get_cuda_gpus():
    global CUDA_DEVICES
    visible_devices = os.environ.get("CUDA_VISIBLE_DEVICES", None)
    if visible_devices is None:
        try:
            _nvidia_smi_proc = subprocess.run(
                ["nvidia-smi", "--list-gpus"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            output = _nvidia_smi_proc.stdout.decode("utf-8")
            CUDA_DEVICES = re.findall(r"GPU ([0-9]*):", output)
        except FileNotFoundError:
            CUDA_DEVICES = []
    else:
        if visible_devices == "-1":
            CUDA_DEVICES = []
        try:
            CUDA_DEVICES = [str(int(d)) for d in visible_devices.split(",")]
        except ValueError:
            CUDA_DEVICES = []


get_cuda_gpus()


def _ram_in_use_gb():
    vm = psutil.virtual_memory()
    return (vm.total - vm.available) / _BYTES_PER_GB


def _filter_cmds_remaining(commands, data_dir):
    out_commands = set()
    for cmd in commands:
        for arg in cmd.args + cmd.extra_outputs:
            if isinstance(arg, Out) and not os.path.exists(
                os.path.join(data_dir, arg.filename)
            ):
                out_commands.add(cmd)
    return out_commands


def _filter_cmds_ready(commands, data_dir):
    out_commands = set()
    for cmd in commands:
        ready = True
        for arg in cmd.args + cmd.extra_inputs:
            if isinstance(arg, In) and not os.path.exists(
                os.path.join(data_dir, arg.filename)
            ):
                ready = False
        if ready:
            out_commands.add(cmd)
    return out_commands


def _filter_cmds_ram(commands, *, reserved_ram_gb, ram_gb_cap):
    out_commands = set()
    for cmd in commands:
        if max(reserved_ram_gb, _ram_in_use_gb()) + cmd.ram_gb <= ram_gb_cap:
            out_commands.add(cmd)
    return out_commands


def _sort_cmds(commands):
    def key(cmd) -> Tuple[List[int], float, float]:
        priority_as_list = cmd.priority
        if not isinstance(priority_as_list, (list, tuple)):
            priority_as_list = [priority_as_list]

        return ([-prio for prio in priority_as_list], cmd.warmup_time, cmd.ram_gb)

    return sorted(list(commands), key=key)


def _cmd_to_args(cmd, data_dir, tmp_data_dir):
    args = []
    for arg in cmd.args:
        if isinstance(arg, In):
            assert not arg.filename.startswith("/")
            arg = os.path.join(data_dir, arg.filename)
            os.makedirs(os.path.split(arg)[0], exist_ok=True)
        elif isinstance(arg, (Out, FileArg)):
            assert not arg.filename.startswith("/")
            # Use temprorary directory here
            arg = os.path.join(tmp_data_dir, arg.filename)
            os.makedirs(os.path.split(arg)[0], exist_ok=True)
        args.append(str(arg))
    return args


def _filter_completed(running):
    for p in running:
        p[1].poll()
    completed = [p for p in running if p[1].returncode is not None]
    now_running = [p for p in running if p not in completed]
    assert len(completed) + len(now_running) == len(running)
    return now_running, completed


def _cmd_name(cmd):
    args = []
    for arg in cmd.args:
        if isinstance(arg, (In, Out)):
            args.append(arg.filename)
        else:
            args.append(str(arg))
    name = " ".join(args).replace("/", ":")
    if len(name) > 200:
        name = name[:200]
    return name


def _run_process(args, *, gpus, ram_gb, stdout, stderr):
    global next_cuda_device
    env = os.environ.copy()
    if _USING_SLURM:
        args = ["srun", f"--mem={int(math.ceil(ram_gb))}G", "--"] + args
    elif gpus is not None:
        env["CUDA_VISIBLE_DEVICES"] = gpus
    elif len(CUDA_DEVICES) > 1:
        env["CUDA_VISIBLE_DEVICES"] = str(CUDA_DEVICES[next_cuda_device])
        next_cuda_device = (next_cuda_device + 1) % len(CUDA_DEVICES)
    return subprocess.Popen(args, stdout=stdout, stderr=stderr, env=env)


@dataclass
class Context:

    commands: set = field(default_factory=set)
    running: list = field(default_factory=list)
    # data_dir: str = os.path.expanduser("~/exp_data")
    data_dir: str = f"{os.getcwd()}/data"
    _vm_percent_cap: float = 90.0
    max_concurrent_jobs: int or None = psutil.cpu_count()
    warmup_deadline: float = time.monotonic()
    reserved_ram_gb: float = _ram_in_use_gb()

    @property
    def _tmp_data_dir(self):
        return f"{self.data_dir}_tmp"

    @property
    def ram_gb_cap(self):
        return (
            self._vm_percent_cap
            * psutil.virtual_memory().total
            / (100.0 * _BYTES_PER_GB)
        )

    @property
    def vm_percent_cap(self):
        return self._vm_percent_cap

    @vm_percent_cap.setter
    def vm_percent_cap(self, value):
        self._vm_percent_cap = value

    def cmd(self, command):
        self.commands.add(command)

    def run_all(self, filename="exps.py"):
        """Runs all commands listed in the file."""
        done = False
        while not done:
            ready_cmds, done = self._refresh_commands(filename)
            if self._ready() and ready_cmds:
                self.run_cmd(ready_cmds[0])
                done = False
            if not _USING_SLURM:
                self._terminate_if_oom()
            self.running, completed = _filter_completed(self.running)
            if self.running:
                done = False
            if not completed:
                # Don't hard-loop
                time.sleep(0.2)
            self._process_completed(completed)

    def _ready(self):
        """Checks global readiness conditions."""
        if (
            self.max_concurrent_jobs is not None
            and len(self.running) >= self.max_concurrent_jobs
        ):
            return False
        if time.monotonic() < self.warmup_deadline:
            return False
        return True

    def _refresh_commands(self, filename):
        """Reloads, filters, and sorts the commands"""
        old_commands = self.commands
        self.commands = set()
        try:
            with open(filename) as f:
                content = f.read()
                exec(content, {})
        except Exception as exc:
            if isinstance(exc, KeyboardInterrupt):
                raise exc
            else:
                try:
                    line_num = sys.exc_info()[2].tb_next.tb_lineno
                    print(f"Error in exps.py (line {line_num}):")
                    print(exc)
                    print(">>", content.split("\n")[line_num - 1])
                except AttributeError:
                    print(exc)
                self.commands = old_commands
        ready, done = self._filter_commands(self.commands)
        return _sort_cmds(ready), done

    def _filter_commands(self, commands):
        """Filters the commands to find only those that are ready to run"""
        needs_output = _filter_cmds_remaining(commands, self.data_dir)
        has_inputs = _filter_cmds_ready(needs_output, self.data_dir)
        if needs_output and not has_inputs:
            print("Commands exist without any way to acquire inputs:", needs_output)
        if _USING_SLURM:
            fits_in_ram = has_inputs
        else:
            fits_in_ram = _filter_cmds_ram(
                has_inputs,
                reserved_ram_gb=self.reserved_ram_gb,
                ram_gb_cap=self.ram_gb_cap,
            )
        not_running = self._filter_cmds_running(fits_in_ram)
        return not_running, not bool(needs_output)

    def _filter_cmds_running(self, commands):
        """Filters out running commands"""
        out_commands = set()
        for cmd in commands:
            running = False
            for (running_cmd, proc) in self.running:
                if cmd == running_cmd:
                    running = True
                    break
            if not running:
                out_commands.add(cmd)
        return out_commands

    def run_cmd(self, cmd):
        """Sets temp files and starts a process for cmd"""
        self.reserved_ram_gb += cmd.ram_gb
        cmd_dir = os.path.join(self._tmp_data_dir, "pipes", _cmd_name(cmd))
        os.makedirs(cmd_dir, exist_ok=True)
        stdout = open(os.path.join(cmd_dir, "stdout.txt"), "w")
        stderr = open(os.path.join(cmd_dir, "stderr.txt"), "w")
        args = _cmd_to_args(cmd, self.data_dir, self._tmp_data_dir)
        print(" ".join(args))
        proc = _run_process(
            args, gpus=cmd.gpus, ram_gb=cmd.ram_gb, stdout=stdout, stderr=stderr
        )
        print(proc.pid)
        self.warmup_deadline = time.monotonic() + cmd.warmup_time
        self.running.append((cmd, proc))
        return proc

    def _terminate_if_oom(self):
        """Terminates processes if over ram cap"""
        gb_free = self.ram_gb_cap - _ram_in_use_gb()

        def total_time(cmd_proc):
            cmd, proc = cmd_proc
            times = psutil.Process(proc.pid).cpu_times()
            return (
                times.user + times.system + times.children_user + times.children_system
            )

        by_total_time = sorted(self.running, key=total_time)
        for (running_cmd, proc) in by_total_time:
            try:
                mem = psutil.Process(proc.pid).memory_full_info()
            except psutil.ZombieProcess:
                continue
            ram_gb = (mem.pss + mem.uss) / _BYTES_PER_GB
            if ram_gb > running_cmd.ram_gb:
                print(
                    f"Command exceeded memory limit "
                    f"({ram_gb} > {running_cmd.ram_gb}): "
                    f"{_cmd_name(running_cmd)}"
                )
                self.reserved_ram_gb -= running_cmd.ram_gb
                running_cmd.ram_gb = ram_gb
                self.reserved_ram_gb += running_cmd.ram_gb
            if gb_free < 0:
                print(f"Terminating process: {_cmd_name(running_cmd)}")
                proc.terminate()
                gb_free += ram_gb

    def _process_completed(self, completed):
        """Copy outputs from the tmp dir if the process exited successfully"""
        for (cmd, proc) in completed:
            self.reserved_ram_gb -= cmd.ram_gb
            if proc.returncode != 0:
                print(f"Error running {cmd}")
                cmd_dir = os.path.join(self._tmp_data_dir, "pipes", _cmd_name(cmd))
                with open(os.path.join(cmd_dir, "stderr.txt")) as f:
                    print(f.read())
            else:
                print(f"Command complete: {cmd}")
                for arg in cmd.args + cmd.extra_outputs:
                    if isinstance(arg, Out):
                        tmp = os.path.join(self._tmp_data_dir, arg.filename)
                        final = os.path.join(self.data_dir, arg.filename)
                        os.makedirs(os.path.split(final)[0], exist_ok=True)
                        try:
                            if os.path.isdir(tmp):
                                shutil.copytree(tmp, final, dirs_exist_ok=True)
                            else:
                                shutil.copy2(tmp, final)
                        except Exception as exc:
                            if isinstance(exc, KeyboardInterrupt):
                                raise exc
                            print(f"Could not copy output {tmp} for command {cmd}")


GLOBAL_CONTEXT = Context()


def cmd(
    *args,
    extra_outputs=tuple(),
    extra_inputs=tuple(),
    warmup_time: float = 1.0,
    ram_gb: float = 4,
    priority: Union[int, List[int], Tuple[int, ...]] = 10,
    gpus: Union[str, None] = None,
):
    """Add a command to be run by the GLOBAL_CONTEXT"""
    if isinstance(priority, list):
        priority = tuple(priority)
    GLOBAL_CONTEXT.cmd(
        Cmd(
            args=tuple(args),
            extra_outputs=tuple(extra_outputs),
            extra_inputs=tuple(extra_inputs),
            warmup_time=warmup_time,
            ram_gb=ram_gb,
            priority=priority,
            gpus=gpus,
        )
    )


if __name__ == "__main__":
    print("You probably meant to call src/runexp.py")
    command = [sys.executable, "src/runexp.py"]
    print("Executing ", " ".join(command))
    os.execv(command[0], command)
