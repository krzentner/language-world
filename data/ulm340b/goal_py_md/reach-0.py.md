

The "steps" for `reach` are:

>   1. Put gripper above the target location
>   2. Move gripper to the target location

Note that for the steps above, you should use `robot.move_gripper`, not
`robot.close_gripper`. The robot's gripper should stay open at all times.
You will need to decide for yourself how to break down the problem into
conditions and actions.

### Helpful instructions

The following is a description of the `check` and `robot.move_gripper`
functions.

The function `check(condition)` returns True or False depending on whether the
given condition is true in the environment.
For example, `check("the ball is red")` returns True if the ball is red,
and False otherwise.

The function `robot.move_gripper(location)` tells the robot to
move its gripper to a specified location.
The location string can be one of the following:

* "around the (object)": Move the gripper to the space around the specified object, such as "around the cube"
* "in front of the (object)": Move the gripper to the space in front of the specified object, such as "in front of the ball"
* "vertically aligned with (object)": Move the gripper to the space vertically aligned with the specified object, such as "vertically aligned with the block"
* "above the (object)": Move the gripper to the space above the specified object, such as "above the cube"
* "below the (object)": Move the gripper to the space below the specified object, such as "below the ball"
* "near the (object)": Move the gripper to the space near the specified object, such as "near the block"
* "left of the (object)": Move the gripper to the space left of the specified object, such as "left of the ball"
* "right of the (object)": Move the gripper to the space right of the specified object, such as "right of the cube"
* "in front of the (object)": Move the gripper to the space in front of the specified object, such as "in front of the block"
* "behind the (object)": Move the gripper to the space behind the specified object, such as "behind the ball"
* "on top of the (object)": Move the gripper to the space on top of the specified object, such as "on top of the block"
* "horizontally aligned with (object)": Move the gripper to the space horizontally aligned with the specified object, such as "horizontally aligned with the ball"