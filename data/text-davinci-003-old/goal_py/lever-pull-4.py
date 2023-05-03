
    # Steps:
    #  1. Put gripper above lever
    #  2. Grab the lever with the gripper
    #  3. Rotate lever up
    # First, put the gripper roughly above lever, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever")
    # If the gripper isn't around the lever, put it around the lever.
    if check("the robot's gripper is not around lever and the robot's gripper is open"):
        robot.move_gripper("around the lever")
    # If the gripper is around the lever, we should be able to rotate it.
    if check("the robot's gripper is around lever and the robot's gripper is closed"):
        robot.move_gripper("up")