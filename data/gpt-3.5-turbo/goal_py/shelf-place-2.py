# Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move the gripper to the target location and open the gripper to place
    #     the block
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and closed, maybe we can grab it by
    # lifting the gripper and moving it to the target location.
    if check("the robot's gripper is around the block and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, open the gripper to release
    # the block.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the block", open_gripper=True)