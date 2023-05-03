
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around block
    #  4. Lift block above shelf
    #  5. Place block on shelf
    # First, put the gripper above the block, so that it doesn't bump into it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and closed, raise it up above the shelf.
    # We don't want to grab the block from above, since it will be unstable.
    if check("the block is above the shelf"):
        robot.move_gripper("above the target location")
    # Now that the gripper is above the target location, lower the gripper onto
    # the shelf and release the block.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("left of the target location", open_gripper=True)