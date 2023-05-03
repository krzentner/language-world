
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the lever up
    # First, put the gripper roughly above the lever so that it can grab the
    # lever.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    # If the gripper is above the lever, try to grab the lever,
    if check("the robot's gripper is above the lever and the robot's gripper is open"):
        robot.grab("lever")
    # If we grabbed the lever we can just rotate it up.
    if check("the robot's gripper is above the lever and the robot's gripper is closed"):
        robot.rotate("lever")