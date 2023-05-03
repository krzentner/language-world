

Then, the rest of the program:

```
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Pick up the block
    #  4. Move block to destination
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above the block and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
    # If the gripper is near the target location, release the block by
    # opening the gripper.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location", close_gripper=False)
```