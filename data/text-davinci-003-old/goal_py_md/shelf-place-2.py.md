

Steps:
1. Put gripper above block
2. Drop gripper around block
3. Grip block with gripper
4. Move block above target location
5. Place block in target position

# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Grip block with gripper
    #  4. Move block above target location
    #  5. Place block in target position
    # First, put the gripper above the block so that it can be grabbed.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper is not around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block, grab the block by closing the gripper.
    if check("the robot's gripper is near the block and the gripper is closed"):
        robot.move_gripper("above the target location")
    # Now, move the block to the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location")
    # Once the block is lined up with the target location, place it on the shelf.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("near the target location", open_gripper=True)