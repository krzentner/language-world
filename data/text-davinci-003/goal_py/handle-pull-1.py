
    # Steps:
    #  1. Put gripper above handle
    #  2. Push gripper down onto handle
    #  3. Pull up handle
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("above handle")
    # If the handle is not below the gripper, push the gripper down onto the
    # handle.
    if check("the handle is not below the robot's gripper and the robot's gripper is not above handle"):
        robot.move_gripper("below handle", close_gripper=True)
    # If the handle is below the gripper, close the gripper onto the handle and
    # pull it up.
    if check("the handle is below the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("above handle")