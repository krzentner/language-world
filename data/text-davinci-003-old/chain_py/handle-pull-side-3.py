
    # Steps:
    #  1. Put gripper right of the handle
    #  2. Start pulling up on the handle
    #  3. Pull harder to open the handle
    # To start, put the robot's gripper to the right of the handle.
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle from the side")
    # If the robot's gripper is near the handle, we can start pulling on it.
    if check("the robot's gripper is near the handle"):
        robot.pull("up on the handle")
    # As we're pulling harder on the handle, the handle will open more and more.
    # So keep pulling until it's open.
    if check("the handle is still not open"):
        robot.pull("harder to open the handle")