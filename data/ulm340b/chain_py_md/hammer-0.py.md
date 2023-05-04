

Here are some examples that use our existing tasks:

```
if not check("the nail is not horizontal"):
    reach(robot)
if not check("the nail is horizontal"):
    pick_place(robot)
```

and here are some examples of commands you can call on `robot`:

```
robot.grab("hammer")
robot.drop("hammer on nail")
robot.grab("hammer")
robot.pull("nail out")
```

This task can be completed with 4 steps and 22 lines of code,
but I would like you to complete it with fewer steps or fewer lines of code if possible.
"""

import sys

# Tasks: [('button-press-topdown', 22),
#  ('door-open', 26),
#  ('reach', 14),
#  ('drawer-close', 24),
#  ('drawer-open', 38),
#  ('peg-insert-side', 45),
#  ('pick-place', 35),
#  ('push', 38),
#  ('window-close', 34),
#  ('window-open', 33),
#  ('hammer', 100)]
def hammer(robot):
    """hit the nail with the hammer"""
    """
    Hammer the nail

    robot.drop("gripper on hammer")
    robot.place("hammer near nail")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
    robot.grab("hammer")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
    robot.grab("hammer")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
    robot.grab("hammer")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
    robot.grab("hammer")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
    robot.grab("hammer")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
    robot.grab("hammer")
    robot.drop("hammer on nail")
    robot.slide("hammer to the left")
