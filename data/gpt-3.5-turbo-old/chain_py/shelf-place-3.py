# Steps:
    #  1. Put gripper above the block
    #  2. Lower the gripper onto the block
    #  3. Close the gripper around the block
    #  4. Move the block to the target location
    # First, put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, lower it onto the block.
    if check("the robot's gripper is above the block and the robot's gripper is not around block"):
        robot.drop("gripper onto block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the block to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is holding the block"):
        robot.place("block at goal")