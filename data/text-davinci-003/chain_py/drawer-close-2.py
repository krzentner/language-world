
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push the drawer closed
    # Just like with opening the drawer, we need to put the gripper above the
    # drawer handle before we can grab it.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is vertically aligned with the drawer handle, close the
    # gripper around it so that we can grab it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    # Once the gripper is around the drawer handle, just push the drawer closed.
    if check("the robot's gripper is around drawer handle"):
        robot.push("towards drawer")