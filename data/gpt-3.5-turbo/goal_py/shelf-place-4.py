# Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around block
    #  4. Move block to target location
    # First, put the gripper above the block to avoid hitting it with the gripper.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and closed, we can move it to the target location.
    if check("the robot's gripper is around the block and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")
    # If the gripper is near the target location, we can release the block by opening the gripper.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.open_gripper()