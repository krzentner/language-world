
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper roughly above the door handle, so that we don't
    # bump it while trying to grab it.
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle")
    # If the gripper isn't around the door handle, put it around the door handle.
    if check("the robot's gripper is not around the door handle and the robot's gripper is open"):
        robot.move_gripper("near the door handle", close_gripper=True)
    # If the gripper is near the door handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above the door handle and the robot's gripper is closed"):
        robot.move_gripper("left of the door handle")