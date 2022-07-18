import collections
import multiprocessing as mp
import threading
import queue
import functools
import os
import warnings

USE_THREADS = False

class OtherProcessException(Exception):

  def __init__(self, inner):
    self.inner = inner


class ProcessCloseException(Exception):
  pass


class ProcessHandle:

  def __init__(self, incoming=None, outgoing=None):
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
    result = None
    while not has_send or result is None:
      if result is None:
        result = self.recv(block=True,
                           timeout=step_timeout if not has_send else None)
      if not has_send:
        has_send = self.send(item,
                             block=True,
                             timeout=step_timeout if result is None else None)
    return result

  def _flip(self):
    return ProcessHandle(incoming=self.outgoing, outgoing=self.incoming)


class Subprocess(ProcessHandle):

  def __init__(self, target, args, kwargs, use_thread=None, scope=None):
    super().__init__()
    if not isinstance(use_thread, bool):
      use_thread = USE_THREADS
    kwargs.update({
        'parent': self._flip()
    })
    tgt = functools.partial(_subprocess_wrapper, self.incoming, target)
    self.thread = None
    self.process = None
    args_kwargs = {'args_kwargs': (args, kwargs)}
    if scope is None:
      try:
        scope = SCOPE_STACK[-1]
      except IndexError:
        raise TypeError("Must enter at least one easy_process.Scope")
    scope.processes.append(self)
    if use_thread:
      self.thread = threading.Thread(target=tgt,
                                     kwargs=args_kwargs,
                                     daemon=False)
      self.thread.start()
    else:
      self.process = mp.Process(target=tgt,
                                kwargs=args_kwargs,
                                daemon=False)
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
    force_close_processes(self.processes)
    self.processes = []
    SCOPE_STACK.pop()


def _force_close_process(proc, exception):
  assert proc.process
  # The pipe to the child process is full.
  # We can't know with certainty what state it's in (it might be blocked
  # on sending to us, it might be crashed).
  # This state is already unusual, so we can afford to spend some time.
  # However, we might be crashing, so we need it to close or we'll block
  # when multiprocessing joins on the process.
  # First, try to see if the process is already dead:
  proc.process.join(1)
  if not proc.process.is_alive():
    return
  # Second, try to send the exception with a timeout.
  proc.send_exception(exception, block=True, timeout=10)
  if not proc.process.is_alive():
    return
  # Then, give it ten seconds to close
  proc.process.join(10)
  if not proc.process.is_alive():
    return
  # Third, send SIGTERM
  proc.process.terminate()
  proc.process.join(10)
  if not proc.process.is_alive():
    return
  proc.process.kill()

def force_close_processes(processes):
  exception = ProcessCloseException()
  stuck_procs = [proc for proc in processes
                 if not proc.send_exception(exception, block=False)]
  for proc in stuck_procs:
    if proc.process:
      _force_close_process(proc, exception)
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
    return Subprocess(func, args, kwargs)
  return subprocess_wrapper
