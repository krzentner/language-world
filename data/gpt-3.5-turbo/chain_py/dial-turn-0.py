# Steps:
    #  1. Put gripper around dial handle
    #  2. Turn the dial the desired amount
    # To turn the dial, we need to grab onto the handle of the dial and turn it.
    # First, put the gripper around the dial handle.
    if check("the robot's gripper is not around the dial handle"):
        robot.grab("dial handle")
    # Once we have a grip on the dial handle, turn it the desired amount.
    if check("the robot's gripper is around the dial handle"):
        robot.turn("dial to desired position")