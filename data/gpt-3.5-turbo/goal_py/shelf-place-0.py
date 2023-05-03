# Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to target location
    # First, put the gripper roughly above the block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block and closed, move it to the target location and place the block there.
    if check("the robot's gripper is around block and the robot's gripper is closed"):
        robot.move_gripper("above the target location", close_gripper=False)