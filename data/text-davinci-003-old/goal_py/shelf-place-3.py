
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper to pick up block
    #  4. Move block to target location
    # If the gripper isn't above the block, we should move it up to the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't near the block, move it closer to the block to start
    # picking it up.
    if check("the robot's gripper is above the block but not near the block"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block, close the gripper all the way to pick up
    # the block.
    if check("the robot's gripper is near the block"):
        robot.move_gripper("above the target shelf")