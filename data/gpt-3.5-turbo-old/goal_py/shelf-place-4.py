# Steps:
    #  1. Put gripper roughly above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move block to target location
    # First, put the gripper roughly above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and closed, lift it up and move it to the
    # target location.
    if check("the robot's gripper is around block"):
        robot.move_gripper("near the target location")