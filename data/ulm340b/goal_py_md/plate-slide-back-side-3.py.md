

The robot's functions to check the positions of objects are:

```
robot.check_position_vertical
robot.check_position_horizontal
robot.check_position_in_front
robot.check_position_left_of
robot.check_position_right_of
```

The function `robot.check_position_vertical` returns `True` if the robot's gripper is vertically aligned with an object.

The function `robot.check_position_horizontal` returns `True` if the robot's gripper is horizontally aligned with an object.

The function `robot.check_position_in_front` returns `True` if the robot's gripper is forward aligned with an object (as in the peg's handle).

The function `robot.check_position_left_of` returns `True` if the robot's gripper is left of an object.

The function `robot.check_position_right_of` returns `True` if the robot's gripper is right of an object.

The robot's function to move the gripper is `robot.move_gripper`:

```
robot.move_gripper("vertically aligned with plate", close_gripper=True)
```

The arguments of `robot.move_gripper` are the position to move the gripper towards and whether to close the gripper or not.

Note that you should only use the functions `robot.check_position_*` to check the positions of the objects.
For example, the statement:

```
if check("the robot's gripper is horizontally aligned with plate"):
```

is illegal, while the statement:

```
if robot.check_position_horizontal("plate"):
```

is legal. You can look at the implementations of previous examples for more details.

To begin, please write a program to push the plate sideways into the target location by putting the gripper in front of the plate and moving it left to push the plate.

Begin with the text:

```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push the plate back
    if robot.check_position_in_front("plate"):
        robot.move_gripper("vertically aligned with plate", close_gripper=True)
    if check("the robot's gripper is horizontally aligned with plate"):
        robot.move_gripper("left of