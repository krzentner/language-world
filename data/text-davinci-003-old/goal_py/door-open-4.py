
    # Steps:
    #  1. Put Gripper above door handle
    #  2. Drop Gripper around door handle
    #  3. Pull open the door
    # First, put the gripper roughly above door handle, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle")
    # If the gripper isn't around the door handle, put it around the door handle.
    if check("the robot's gripper is not around door handle and the robot's gripper is open"):
        robot.move_gripper("near the door handle", close_gripper=True)
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("left of the door handle")