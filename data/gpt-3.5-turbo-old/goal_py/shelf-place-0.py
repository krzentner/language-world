# Steps:
    #  1. Put gripper above the block
    #  2. Grab the block with the gripper
    #  3. Lift the block off the shelf
    #  4. Move the block to above the target location
    #  5. Lower the block onto the target location
    # First, put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper is not around the block and is above the block, put it around the block.
    if check("the robot's gripper is above the block and the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("almost vertically aligned with the block", close_gripper=True)
    # If the gripper is around the block and the block is still on the shelf, lift the block off the shelf.
    if check("the robot's gripper is around the block and the block is still on the shelf"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, place the block there by lowering the gripper.
    if check("the robot's gripper is above the target location and the robot's gripper is holding the block"):
        robot.move_gripper("above the target location", close_gripper=False)