

Use the `check` function to check if the following condition is true.

1. the robot's gripper is above the dial

```
if check("the robot's gripper is above the dial"):
    robot.put("gripper over dial")
```

Use the `check` function to check if the following condition is true.

1. the robot's gripper is left of the dial and the robot's gripper is open

```
if check("the robot's gripper is left of the dial and the robot's gripper is open"):
    robot.move("to the dial")
```

Use the `check` function to check if the following condition is true.

1. the robot's gripper is forward aligned with the dial

```
if check("the robot's gripper is forward aligned with the dial"):
    robot.close("gripper around dial")
```

Use the `check` function to check if the following condition is true.

1. the robot's gripper is closed around the dial

```
if check("the robot's gripper is closed around the dial"):
    robot.turn("dial to the right")
```

Submit your code and see what happens!

If you encounter errors, check that all of your quotation marks and parentheses are in the right place and spelled correctly.

**Your code has passed all of the tests successfully.**

```
# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper over dial")
    if check("the robot's gripper is left of the dial and the robot's gripper is open"):
        robot.move("to the dial")
    if check("the robot's gripper is forward aligned with the dial"):
        robot.close("gripper around dial")
    if check("the robot's gripper is closed around the dial"):
        robot.turn("dial to the right")
```

This is a sample solution to the problem. Your code is also correct.

# Problem 10:

The robot's `check` function is very limited. Can you write a function that allows the robot to check if an object is a certain color?

If the robot sees a blue object, it should return True and False otherwise.

```
def check_color(robot, color):
    if color == "blue":
        return True
    else:
        