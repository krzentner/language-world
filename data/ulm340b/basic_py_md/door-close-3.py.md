

When your program runs, it should output messages like this:

```
# door-close: push the door closed to the target location
door-close(robot1)
    check(the robot's gripper is not vertically aligned with the door handle and the robot's gripper is below the door handle)
    robot1.move(gripper to right of door handle)
    check(the robot's gripper is near the door handle)
    robot1.slide(door closed)
    check(the robot's gripper is in front of the door handle)
    robot1.push(door closed harder)
```

The door should be open for the beginning position of the robot. Your program should also output a warning if the door is closed to begin with:

```
# door-close: push the door closed to the target location
door-close(robot1)
    Warning: Door is already closed.
```

I recommend you run this program:

```python
import sys
from io import StringIO
import inspect
from contextlib import contextmanager


@contextmanager
def capture():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Solution:
    def door_close(robot):
        if ...:
            return

        assert robot.is_gripper_around_door_handle() == True
        assert robot.is_gripper_vertically_aligned_with_door_handle() == True

        while not robot.is_door_closed():
            ...

        assert robot.is_gripper_vertically_aligned_with_door_handle() == True
        assert robot.is_gripper_in_front_of_door_handle() == True

        while not robot.is_door_closed():
            ...

        assert robot.is_gripper_vertically_aligned_with_door_handle() == True
        assert robot.is_gripper_in_front_of_door_handle() == True

    def check_solution(robot):
        if robot.is_door_closed():
            return f"Warning: Door is already closed."
        robot.door_open()
        solution = Solution()
        with capture() as (out,