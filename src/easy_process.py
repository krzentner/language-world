import collections
import multiprocessing as mp
import threading
import queue
import functools
import sys
import os

USE_THREADS = False
CHILD_PROCESSES = collections.defaultdict(list)

_prev_excepthook = sys.excepthook
def close_child_processes(exctype, value, traceback):
  for proc in CHILD_PROCESSES[os.getpid()]:
    proc.send_exception(value, block=False)
  _prev_excepthook(exctype, value, traceback)
sys.excepthook = close_child_processes


class OtherProcessException(Exception):

  def __init__(self, inner):
    self.inner = inner


class ProcessHandle:

  def __init__(self, incoming=None, outgoing=None):
    self.incoming = incoming or mp.Queue(1)
    self.outgoing = outgoing or mp.Queue(1)
    # If we crash from an exception with a full queue, we would rather not
    # hang forever, so we would like the process to close without flushing
    # the queues.
    # That's what cancel_join_thread does.
    self.outgoing.cancel_join_thread()
    self.incoming.cancel_join_thread()

  def send(self, item, block=True, timeout=None):
    self.outgoing.put(item, block, timeout)

  def send_exception(self, exception, block=True, timeout=None):
    self.outgoing.put(OtherProcessException(exception), block, timeout)

  def recv(self, block=True, timeout=None):
    result = self.incoming.get(block, timeout)
    if isinstance(result, OtherProcessException):
      raise result.inner
    else:
      return result

  def _flip(self):
    return ProcessHandle(incoming=self.outgoing, outgoing=self.incoming)


class Subprocess(ProcessHandle):

  def __init__(self, target, args, kwargs, use_thread=None):
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
    if use_thread:
      self.thread = threading.Thread(target=tgt,
                                     kwargs=args_kwargs)
      self.thread.start()
    else:
      CHILD_PROCESSES[os.getpid()].append(self)
      self.process = mp.Process(target=tgt,
                                kwargs=args_kwargs,
                                daemon=False)
      self.process.start()


def _subprocess_wrapper(outgoing, target, args_kwargs):
  try:
    return target(*args_kwargs[0], **args_kwargs[1])
  except Exception as ex:
    print(ex)
    outgoing.put(OtherProcessException(ex), block=True)
    raise ex


def subprocess_func(func):
  @functools.wraps(func)
  def subprocess_wrapper(*args, **kwargs):
    return Subprocess(func, args, kwargs)
  return subprocess_wrapper
