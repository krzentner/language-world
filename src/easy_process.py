import collections
import multiprocessing as mp
import threading
import queue
import functools
import os
import warnings
import time

USE_THREADS = True
DEFAULT_TIMEOUT = 1e5
USE_FASTER_FIFO = False


class OtherProcessException(Exception):
    def __init__(self, inner):
        self.inner = inner


class ProcessCloseException(Exception):
    pass


class ProcessHandle:
    def __init__(self, incoming=None, outgoing=None):
        if USE_FASTER_FIFO:
            import faster_fifo

            self.incoming = incoming or faster_fifo.Queue()
            self.outgoing = outgoing or faster_fifo.Queue()
        else:
            self.incoming = incoming or mp.Queue(1)
            self.outgoing = outgoing or mp.Queue(1)
        self.incoming.cancel_join_thread()
        self.outgoing.cancel_join_thread()

    def send(self, item, block=True, timeout=None):
        try:
            self.outgoing.put(item, block, timeout)
            return True
        except queue.Full:
            return False

    def send_exception(self, exception, block=True, timeout=None):
        try:
            self.outgoing.put(OtherProcessException(exception), block, timeout)
            return True
        except queue.Full:
            return False

    def recv(self, block=True, timeout=None):
        try:
            result = self.incoming.get(block, timeout)
        except queue.Empty:
            result = None
        if isinstance(result, OtherProcessException):
            raise result.inner
        elif isinstance(result, ProcessCloseException):
            raise result
        else:
            return result

    def sendrecv(self, item, step_timeout=0.1):
        has_send = False
        results = []
        while not has_send and not results:
            if not has_send:
                has_send = self.send(item, block=True, timeout=step_timeout)
            msg = self.recv(block=True, timeout=step_timeout)
            proc = getattr(self, "process", None)
            if proc and not proc.is_alive():
                print("SUBPROCESS HARD FAULT")
            if msg is not None:
                results.append(msg)
        return results

    def _flip(self):
        return ProcessHandle(incoming=self.outgoing, outgoing=self.incoming)


class Subprocess(ProcessHandle):
    def __init__(self, target, *, args=(), kwargs, use_thread=None, scope=None):
        super().__init__()
        if not isinstance(use_thread, bool):
            use_thread = USE_THREADS
        kwargs.update({"parent": self._flip()})
        tgt = functools.partial(_subprocess_wrapper, self.incoming, target)
        self.thread = None
        self.process = None
        args_kwargs = {"args_kwargs": (args, kwargs)}
        if scope is None:
            try:
                scope = SCOPE_STACK[-1]
            except IndexError:
                raise TypeError("Must enter at least one easy_process.Scope")
        scope.processes.append(self)
        if use_thread:
            self.thread = threading.Thread(target=tgt, kwargs=args_kwargs, daemon=False)
            self.thread.start()
        else:
            self.process = mp.Process(target=tgt, kwargs=args_kwargs, daemon=False)
            self.process.start()

    def close(self, terminate=False):
        self.send_exception(ProcessCloseException())
        if self.process and terminate:
            self.process.terminate()


SCOPE_STACK = []


class Scope:
    def __init__(self):
        self.processes = []

    def spawn(self, target, args, kwargs, use_thread=None):
        assert self in SCOPE_STACK
        process = Subprocess(target, args, kwargs, use_thread, scope=self)
        return process

    def __enter__(self):
        SCOPE_STACK.append(self)

    def __exit__(self, exc_type, exc_value, traceback):
        assert SCOPE_STACK[-1] is self
        self.close()
        SCOPE_STACK.pop()

    def close(self):
        force_close_processes(self.processes)
        self.processes = []


def _alive_procs(procs, timeout=0.1):
    for proc in procs:
        proc.process.join(timeout)
    return [proc for proc in procs if proc.process.is_alive()]


def force_close_processes(processes):
    exception = ProcessCloseException()
    stuck_procs = [proc for proc in processes if proc.process]

    # Try to send the exception for 10 seconds.
    for i in range(100):
        for proc in stuck_procs:
            proc.send_exception(exception, block=False)
        stuck_procs = _alive_procs(stuck_procs, timeout=0.1)
        if not stuck_procs:
            break

    # Send SIGTERM
    for proc in stuck_procs:
        proc.process.terminate()
    stuck_procs = _alive_procs(stuck_procs, timeout=10)

    for proc in stuck_procs:
        proc.process.kill()
    # Block on joining everything to avoid errors below
    stuck_procs = _alive_procs(stuck_procs, timeout=None)

    for proc in processes:
        if proc.process:
            proc.process.close()
        else:
            assert proc.thread is not None
            # We can't do much to a thread.
            # Just keep trying to send an exception until the thread isn't alive
            # anymore.
            # Loop in case the thread crashes while we're waiting for it to receive
            # the exception.
            while proc.thread.is_alive():
                if proc.send_exception(exception, block=True, timeout=1):
                    break


def _subprocess_wrapper(outgoing, target, args_kwargs):
    # If we crash from an exception with a full queue, we would rather not
    # hang forever, so we would like the process to close without flushing
    # the outgoing queue.
    # That's what cancel_join_thread does.
    # It must be called inside the process that sends data, which is why it needs
    # to be called here and not the constructutor.
    outgoing.cancel_join_thread()
    try:
        return target(*args_kwargs[0], **args_kwargs[1])
    except Exception as ex:
        if isinstance(ex, ProcessCloseException):
            return
        else:
            outgoing.put(OtherProcessException(ex), block=True)
        raise ex


def subprocess_func(func):
    @functools.wraps(func)
    def subprocess_wrapper(*args, **kwargs):
        return Subprocess(target=func, args=args, kwargs=kwargs)

    return subprocess_wrapper
