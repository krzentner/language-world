
    # Steps:
    #  1. Put the robot's gripper above the block
    #  2. Move the robot's gripper around the block
    #  3. Close the robot's gripper around the block
    #  4. Move the block to the target location
    # First we need to put the gripper above the block, so that it can grab it
    # without knocking the block off the shelf.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, try to grab it by closing the
    # gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe
    # we grabbed it.
    # Now try to move the block to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at goal")