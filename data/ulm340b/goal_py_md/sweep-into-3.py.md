

and write the body of the function.

The body of each function contains one or more conditional statements, like this:

```
# Steps:
#  1. Put gripper above the cube
#  2. Move the gripper towards the cube
# First, put the gripper above the cube, so that it can start dropping down to
# grab it.
if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")
# Move the gripper towards the cube.
if check("the robot's gripper is above the cube"):
    robot.move_gripper("near the cube")
```

Each conditional statement checks whether the robot's gripper is in a particular situation (such as "`the robot's gripper is near the cube`") and if so, performs an action (such as "`robot.move_gripper('left of the cube')`").

The code above should be read as:

- First, if the robot's gripper is not above the cube, move it above the cube.
- Once the gripper is above the cube, if it is above the cube, move it towards the cube.

There are several different kinds of conditional statements that can be used:

- **Simple if statements**: `if check(...):`
- **Simple if statements with negation**: `if not check(...):`
- **If-else statements**: `if check(...): ... else ...`
- **If-else statements with negation**: `if not check(...): ... else ...`

# Code Instructions

Here are the things you should know:

## What robot.move_gripper(text, [open_gripper=True, close_gripper=True]) can do

The robot can execute "`robot.move_gripper(text)`", where `text` can be the following words:

- `'vertically aligned with cube'`
- `'above cube'`
- `'below cube'`
- `'forward aligned with cube'`
- `'behind cube'`
- `'in front of cube'`
- `'near cube'`
- `'left of cube'`
- `'right of cube'`
- `'horizontally aligned with cube'`
- `'around cube'`
- `'inside cube'`
- `'outside cube'`
- `'vertically aligned with puck'`
- `'above puck'`
- `'below puck'`
- `'forward aligned with puck'`
- `'behind puck'`
- `'in front of