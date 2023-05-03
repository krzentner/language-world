# Steps:
    #  1. Put gripper above block
    #  2. Grab the block with the gripper
    #  3. Move the block to the target location
    #  4. Open the gripper to release the block
    # First, put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True)
    # If the gripper is near the block, move it to the target location.
    if check("the robot's gripper is around the block and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, open the gripper to release
    # the block.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("above the block", open_gripper=True)