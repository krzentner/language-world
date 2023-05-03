
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Pull the handle up
    # To pull the handle up, we need to grab it in the right spot.
    # Put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Grab the handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # Now the gripper is around the handle and can pull it up.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")