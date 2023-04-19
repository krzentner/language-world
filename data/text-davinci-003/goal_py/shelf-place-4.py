
    # Steps:
    #  1. Put gripper slightly above the block
    #  2. Close the gripper around the block
    #  3. Move the block to the target location
    # First, put the gripper slightly above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # When the gripper is nearby the block, close the gripper around it.
    if check("the robot's gripper is almost above the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # Now that the block is in the robot's grasp, it can move it the target
    # location.
    if check("the robot's gripper is above the block"):
        robot.move_gripper("near the target location")