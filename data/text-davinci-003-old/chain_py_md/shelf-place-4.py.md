

The steps would be:

1. Put gripper above the block
2. Drop gripper around the block
3. Close gripper around the block
4. Move the block to the target location

```
# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move the block to the target location
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the block to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at target location")