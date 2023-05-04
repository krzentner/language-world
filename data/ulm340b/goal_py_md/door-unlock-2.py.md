

And fill in the function's body:

```
# Steps:
#  1. Move the robot's gripper to where the door's dial is
#  2. Grasp the door's dial
#  3. Turn the dial to where it can open
```

The `robot` object, which you can call `check` on, represents a robot.
`robot` also supports the `move_gripper` method, which takes in a phrase of
text.

Here are some examples of what the robot understands:

`robot.move_gripper("close to the target")` will move the robot's gripper so
that it is close to the target

`robot.move_gripper("near the red thing")` will move the robot's gripper to
the closest red thing

`robot.move_gripper("in front of the button")` will move the robot's gripper
so that it is in front of the button

`robot.move_gripper("left of the blue thing")` will move the robot's gripper
to the left of the blue thing

`robot.move_gripper("right of the box")` will move the robot's gripper to the
right of the box

`robot.move_gripper("above the goal")` will move the robot's gripper above the
goal

`robot.move_gripper("below the goal")` will move the robot's gripper below the
goal

`robot.move_gripper("around the block")` will move the robot's gripper around
the block

`robot.move_gripper("on the block")` will move the robot's gripper on top of
the block

`robot.move_gripper("vertically aligned with the target")` will move the
robot's gripper to be vertically aligned with the target

`robot.move_gripper("vertically aligned with the rightmost peg")` will move
the robot's gripper to be vertically aligned with the rightmost peg

`robot.move_gripper("horizontally aligned with the target")` will move the
robot's gripper to be horizontally aligned with the target

`robot.move_gripper("horizontally aligned with the leftmost peg")` will move
the robot's gripper to be horizontally aligned with the leftmost peg

`robot.move_gripper("forward aligned with the target")` will move the
robot's gripper to be forward aligned with the target

`robot.move_gripper("forward aligned with the leftmost peg")` will move the
robot's