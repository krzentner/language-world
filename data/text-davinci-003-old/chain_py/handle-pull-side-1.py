
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up on the handle
    # First, if the handle isn't left of the gripper, put the gripper around the
    # handle.
    if check("the handle is not left of the robot's gripper and the robot's gripper is not around the handle"):
        robot.put("gripper around the handle")
    # If the handle is left of the robot's gripper, and the robot's gripper is
    # around the handle, pull up on the handle.
    if check("the handle is left of the robot's gripper and the robot's gripper is around the handle"):
        robot.pull("up on the handle")