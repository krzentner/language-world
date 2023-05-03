# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Grab the block with the gripper
    #  3. Move the block to the target location
    #  4. Release the block by opening the gripper
    # First, put the gripper roughly above the block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block and closed, maybe we can grab it by lifting
    # the gripper.
    if check("the robot's gripper is near the block and the robot's gripper is closed"):
        robot.move_gripper("above the target location", close_gripper=True)
    # If the gripper is above the target location, we can place the block there by
    # opening the gripper.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("open")