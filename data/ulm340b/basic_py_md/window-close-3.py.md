

If `the robot's gripper` is `not vertically aligned with the window handle` and `the robot's gripper` is `below the window handle`:

*   call the function `robot.move("gripper to left of window handle")`.

If `the robot's gripper` is `close to the window handle`:

*   call the function `robot.slide("window right")`.

If `the robot's gripper` is `in front of the window handle`:

*   call the function `robot.push("window right harder")`.

## Question

**`window-close`**

Complete the following code so the robot will close the window to the right.

```
# window-close: slide the window closed to the right
def window_close(robot):
```

If `the robot's gripper` is `not vertically aligned with the window handle` and `the robot's gripper` is `below the window handle`:

*   call the function `robot.move("gripper to left of window handle")`.

If `the robot's gripper` is `close to the window handle`:

*   call the function `robot.slide("window right")`.

If `the robot's gripper` is `in front of the window handle`:

*   call the function `robot.push("window right harder")`.

"""

# This function is written for you and is correct.
def check(condition):
    if condition:
        return True
    else:
        return False

# window-close: slide the window closed to the right
def window_close(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is close to the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

## Answer

**`window-close`**

Complete the following code so the robot will close the window to the right.

```
# window-close: slide the window closed to the right
def window_close(robot):
```

If `the robot's gripper` is `not vertically aligned with the window handle` and `the robot's gripper` is `below the window handle`:

*