# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Move the gripper to the target location
    #  4. Release the block
    # First, put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is around the block, move it to the target location.
    # Close the gripper to make sure we keep control of the block.
    if check("the robot's gripper is around the block and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location", close_gripper=True)
    # If the gripper is at the target location, release the block.
    if check("the robot's gripper is near the target location and the block is not held by the gripper"):
        robot.move_gripper("above the target location", open_gripper=True)