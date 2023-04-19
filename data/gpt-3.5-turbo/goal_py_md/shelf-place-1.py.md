# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper roughly above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Move block to target location
    # First, put the gripper roughly above the block, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block and the block is held securely by the
    # gripper, move it to the target location.
    # We don't need to be careful about the exact position of the block on the
    # shelf, since the gripper can just slide it to the correct spot on the
    # shelf.
    if check("the robot's gripper is around the block"):
        robot.move_gripper("above the target location")