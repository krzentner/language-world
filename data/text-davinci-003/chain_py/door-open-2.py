
    # Steps:
    #  1. Put gripper above door handle
    #  2. Grab door handle with gripper
    #  3. Pull door open
    # First, line up the robot's gripper as seen from above with the door handle.
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    # If the robot's gripper is aligned with the door handle, we can grab it.
    # If it's open, close it around the door handle.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is open"):
        robot.grab("door handle")
    # Now that the gripper is closed around the door handle, we can pull the
    # door open.
    if check("the robot's gripper is closed around door handle"):
        robot.pull("away from door")