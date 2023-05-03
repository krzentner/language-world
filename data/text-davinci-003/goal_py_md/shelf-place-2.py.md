

Then add the steps:

```
# Steps:
#  1. Put gripper above block
#  2. Grab the block with the gripper
#  3. Move the block towards the target location shelf
#  4. Place block on the target shelf

# First, put the gripper above the block.
if check("the robot's gripper is not vertically aligned with the block"):
    robot.move_gripper("vertically aligned with the block", close_gripper=True)

# Once the gripper is lined up above the block, we can grab it by moving
# the gripper down around it.
if check("the robot's gripper is vertically aligned with the block"):
    robot.move_gripper("around the block")

# Once the gripper is around the block, we can move it to the target shelf.
if check("the robot's gripper is around the block"):
    robot.move_gripper("towards the target shelf")

# When the block is close to the target shelf, we can place it on the shelf.
if check("puck is close to the target shelf"):
    robot.move_gripper("above the target shelf")
```