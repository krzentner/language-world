# Steps:
    # 1. Put gripper roughly above the block
    # 2. Grab the block with the gripper
    # 3. Move gripper to target location above shelf
    # 4. Release the block
    # First, put the gripper roughly above the block
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # Move the gripper to the target location above the shelf
    if check("the robot's gripper is not near the target location above the shelf"):
        robot.move_gripper("near the target location above the shelf", close_gripper=True)
    # Once the gripper is near the target location, release the block.
    if check("the robot's gripper is near the target location above the shelf"):
        robot.move_gripper("above the target location above the shelf", close_gripper=False)