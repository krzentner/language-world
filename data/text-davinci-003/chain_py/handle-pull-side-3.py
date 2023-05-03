
    # Steps:
    #  1. Put gripper above the handle
    #  2. Lined up gripper with handle
    #  3. Pull up the handle with gripper
    # First put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle isn't aligned with the gripper from the front, move the
    # gripper to the left until it is aligned with the handle.
    if check("the handle is not forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.move("gripper to left of handle")
    # If the handle is aligned with the gripper, close the gripper around the
    # handle.
    if check("the handle is forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.put("gripper around handle")
    # If the gripper is still aligned with the handle, pull the handle up with
    # the gripper.
    if check("the handle is forward aligned with the robot's gripper and the robot's gripper is closed"):
        robot.pull("handle up")