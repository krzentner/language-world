    # Steps:
    #  1. Put gripper around the handle
    #  2. Pull up on the handle from the side
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, pull up on the handle from the
    # side.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up from the side")