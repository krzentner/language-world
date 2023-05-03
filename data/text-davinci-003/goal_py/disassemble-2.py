
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Wrap the gripper around the wrench
    #  3. Pull the wrench off
    # First, line up the gripper with the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # Once the gripper is roughly lined up with the wrench, we can wrap the
    # gripper around the wrench.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Now that the gripper is around the wrench, we can start pulling the wrench
    # off.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("right of the peg")