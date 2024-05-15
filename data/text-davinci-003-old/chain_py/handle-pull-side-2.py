
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle
    #  3. Pull up handle 
    # We need to first put the gripper above the handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Once the gripper is lined up above the handle, we should be able to grab
    # the handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, we can just pull up the handle.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")