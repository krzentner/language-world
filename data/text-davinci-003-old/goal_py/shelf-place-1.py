
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Move to target location
    #  4. Drop the block at the target location
    # Put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with block"):
        robot.move_gripper("vertically aligned with the block")
    # Grab the block with the gripper.
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is not around block"):
        robot.move_gripper("close to the block")
    # Move the block to the target location.
    if check("the robot's gripper is close to the block"):
        robot.move_gripper("close to the target location")
    # Drop the block at the target location.
    if check("the robot's gripper is close to the target"):
        robot.move_gripper("above the target location", open_gripper=True)