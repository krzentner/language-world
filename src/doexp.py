from dataclasses import dataclass, field
import os
import subprocess
import psutil
import time
import shutil


@dataclass(frozen=True)
class In:
    filename: str


@dataclass(frozen=True)
class Out:
    filename: str


@dataclass(frozen=True)
class Cmd:

    args: tuple
    extra_outputs: tuple
    extra_inputs: tuple
    warmup_time: float = 1.0


@dataclass
class Context:

    commands: set = field(default_factory=set)
    running: list = field(default_factory=list)
    data_dir: str = os.path.expanduser("~/exp_data")
    vm_percent_cap: float = 60.0

    def cmd(self, command):
        self.commands.add(command)

    def run_all(self, filename="exps.py"):
        done = False
        while not done:
            self.commands = set()
            try:
                with open(filename) as f:
                    exec(f.read())
            except Exception as exc:
                if isinstance(exc, KeyboardInterrupt):
                    raise exc
                else:
                    print("Error in exps.py:")
                    print(exc)
            done = True
            for cmd in sorted(self.commands, key=lambda cmd: cmd.warmup_time):
                if self._should_run(cmd):
                    print(f"Starting {cmd}")
                    done = False
                    proc = self.run(cmd)
                    self.running.append((cmd, proc))
                    break
            self.running, completed = _filter_completed(self.running)
            if self.running:
                done = False
            if not completed:
                time.sleep(0.2)
            for (cmd, proc) in completed:
                if proc.returncode != 0:
                    print(f"Error running {cmd}")
                    cmd_dir = os.path.join(self.data_dir, "pipes", cmd_name(cmd))
                    with open(os.path.join(cmd_dir, "stderr.txt")) as f:
                        print(f.read())
                else:
                    print(f"Command complete: {cmd}")
                    for arg in cmd.args + cmd.extra_outputs:
                        if isinstance(arg, Out):
                            tmp = os.path.join(self.data_dir, "tmp", arg.filename)
                            final = os.path.join(self.data_dir, arg.filename)
                            os.makedirs(os.path.split(final)[0], exist_ok=True)
                            try:
                                if os.path.isdir(tmp):
                                    shutil.copytree(tmp, final, dirs_exist_ok=True)
                                else:
                                    shutil.copy2(tmp, final)
                            except Exception as exc:
                                if isinstance(exc, KeyBoardInterrupt):
                                    raise exc
                                print(f"Could not copy output {tmp} for command {cmd}")

    def run(self, cmd):
        cmd_dir = os.path.join(self.data_dir, "pipes", cmd_name(cmd))
        os.makedirs(cmd_dir, exist_ok=True)
        stdout = open(os.path.join(cmd_dir, "stdout.txt"), "w")
        stderr = open(os.path.join(cmd_dir, "stderr.txt"), "w")
        preproc = self._preprocess_cmd(cmd)
        print(" ".join(preproc))
        proc = subprocess.Popen(preproc, stdout=stdout, stderr=stderr)
        print(proc.pid)
        time.sleep(cmd.warmup_time)
        return proc

    def _preprocess_cmd(self, cmd):
        args = []
        for arg in cmd.args:
            if isinstance(arg, In):
                assert not arg.filename.startswith("/")
                arg = os.path.join(self.data_dir, arg.filename)
                os.makedirs(os.path.split(arg)[0], exist_ok=True)
            if isinstance(arg, Out):
                assert not arg.filename.startswith("/")
                arg = os.path.join(self.data_dir, "tmp", arg.filename)
                os.makedirs(os.path.split(arg)[0], exist_ok=True)
            args.append(arg)
        return args

    def _should_run(self, cmd):
        for arg in cmd.args + cmd.extra_inputs:
            if isinstance(arg, In) and not os.path.exists(
                os.path.join(self.data_dir, arg.filename)
            ):
                print(f"Waiting for input file {arg.filename}")
                return False
        for (running_cmd, proc) in self.running:
            if cmd == running_cmd:
                return False
        need_output = False
        for arg in cmd.args + cmd.extra_outputs:
            if isinstance(arg, Out) and not os.path.exists(
                os.path.join(self.data_dir, arg.filename)
            ):
                print(f"Need output {arg.filename}")
                need_output = True
        if need_output and psutil.virtual_memory().percent >= self.vm_percent_cap:
            print("Waiting for free RAM...")
            time.sleep(30)
            return False
        return need_output


def _filter_completed(running):
    for p in running:
        p[1].poll()
    completed = [p for p in running if p[1].returncode is not None]
    now_running = [p for p in running if p not in completed]
    assert len(completed) + len(now_running) == len(running)
    return now_running, completed


def cmd_name(cmd):
    args = []
    for arg in cmd.args:
        if isinstance(arg, (In, Out)):
            args.append(arg.filename)
        else:
            args.append(arg)
    name = " ".join(args).replace("/", ":")
    if len(name) > 200:
      name = name[:200]
    return name


GLOBAL_CONTEXT = Context()


def cmd(*args, extra_outputs=tuple(), extra_inputs=tuple(), warmup_time=1.0):
    GLOBAL_CONTEXT.cmd(
        Cmd(
            args=tuple(args),
            extra_outputs=tuple(extra_outputs),
            extra_inputs=tuple(extra_inputs),
            warmup_time=warmup_time,
        )
    )
