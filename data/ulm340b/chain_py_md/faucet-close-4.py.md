

And add to it until you have a complete program.

"""
import inspect
import sys


class Robot:
    def __init__(self):
        self.state = RobotState()

    def grab(self, what):
        print(f"Grab the {what}")
        self.state._grab(what)

    def place(self, where):
        print(f"Place it {where}")
        self.state._place(where)

    def drop(self, where):
        print(f"Drop it {where}")
        self.state._drop(where)

    def pull(self, where):
        print(f"Pull {what} {where}")
        self.state._pull(where)

    def push(self, where):
        print(f"Push {what} {where}")
        self.state._push(where)

    def align(self, where):
        print(f"Align it to {where}")
        self.state._align(where)

    def move(self, where):
        print(f"Move it {where}")
        self.state._move(where)

    def insert(self, where):
        print(f"Insert it in {where}")
        self.state._insert(where)

    def close(self, what):
        print(f"Close it around {what}")
        self.state._close(what)

    def slide(self, where):
        print(f"Slide it {where}")
        self.state._slide(where)

    def push(self, where):
        print(f"Push {what} {where}")
        self.state._push(where)

    def reach(self, where):
        print(f"Reach to {where}")
        self.state._reach(where)

    def _execute(self, task):
        fn = getattr(self, task.name)
        if inspect.isgeneratorfunction(fn):
            return self._execute_generator(fn, task.options)
        if inspect.iscoroutinefunction(fn):
            import asyncio
            return self._execute_coroutine(asyncio.coroutine(fn), task.options)
        return fn(task.options)

    def _execute_generator(self, fn, options):
        iterator = fn(options)
        next(iterator)
        print(self.state)
        print(self.state)

    def _execute_coroutine(self, fn, options):
       