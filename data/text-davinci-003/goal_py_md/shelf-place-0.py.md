

Then add the code:

```
# Steps:
#  1. Put gripper above block
#  2. Drop gripper around block
#  3. Close gripper around block
#  4. Move block to goal
# First, put the gripper above the block, so that we don't bump it while trying
# to grab it.
if check("the robot's gripper is not above the block"):
    robot.move_gripper("above the block")
# If the gripper isn't around the block, put it around it.
if check("the robot's gripper is not around block and the robot's gripper is open"):
    robot.move_gripper("near the block", close_gripper=True)
# If the gripper is near the block and open, maybe we can grab it by closing
# the gripper.
if check("the robot's gripper is above block and the robot's gripper is closed"):
    robot.move_gripper("near the target location")
```