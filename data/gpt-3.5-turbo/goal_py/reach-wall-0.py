# Steps:
    #  1. Pick up a block with the gripper and put it in front of wall
    #  2. Reach over the wall to the target location
    #  3. Put the block back down
    # We need to first pick up a block with the gripper
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near the block", close_gripper=True) 
    # If the gripper is near the block, move block in front of wall
    if check("the robot's gripper is near block"):
        robot.move_gripper("in front of the wall")
    # Once we have the block in front of the wall, we can reach over the wall
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Finally, we put the block down
    if check("the robot's gripper is above the block and the robot's gripper is closed"):
        robot.move_gripper("in front of the wall", open_gripper=True)