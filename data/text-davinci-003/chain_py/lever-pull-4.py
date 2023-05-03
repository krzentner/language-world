
    # Steps:
    #  1. Put gripper around the lever
    #  2. Rotate the lever up
    # We need to grab the lever before we can pull it.
    # Try to grab the lever from underneath.
    # This will put the gripper around the lever.
    if check("the robot's gripper is not around lever"):
        robot.grab("lever")
    # As long as the lever is still in the robot's gripper, rotate it up.
    if check("the robot's gripper is around lever"):
        robot.rotate("lever up")