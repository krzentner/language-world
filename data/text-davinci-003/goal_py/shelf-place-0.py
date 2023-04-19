
    # Steps:
    #  1. Put gripper above block
    #  2. Place gripper around block
    #  3. Lift and move block to target
    #  4. Drop block in target
    # First, put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
    # If the block moves out of the way, move the gripper above the block again.
    if check("the robot's gripper is not around the block and the robot's gripper is empty"):
        robot.move_gripper("around the block", close_gripper=True)
    # Once the gripper is around the block, we can lift it and carry it to the
    # target.
    if check("the robot's gripper is around the block"):
        robot.move_gripper("near the target")
    # Once we're near the target location, we can drop the block by opening the
    # gripper.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("near the target location", close_gripper=False)