
    # Steps:
    #  1. Put gripper above the basketball
    #  2. Drop gripper around basketball
    #  3. Throw the basketball into the hoop
    # First, put the gripper above the basketball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above basketball"):
        robot.move_gripper("above the basketball")
    # If the gripper isn't around the basketball, put it around the basketball.
    if check("the robot's gripper is not around basketball"):
        robot.move_gripper("near the basketball", close_gripper=True)
    # Once the gripper is around the basketball, just throw it into the hoop.
    if check("the robot's gripper is around basketball"):
        robot.move_gripper("above the hoop")