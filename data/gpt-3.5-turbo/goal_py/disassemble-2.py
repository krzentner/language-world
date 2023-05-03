# Steps:
    #  1. Put gripper above the wrench handle
    #  2. Drop gripper around the wrench handle
    #  3. Close the gripper around the wrench handle
    #  4. Pull the wrench off the peg
    # First, put the gripper mostly above the wrench handle, so that we don't bump
    # into anything while trying to grab it.
    if check("the robot's gripper is not above the wrench handle"):
        robot.move_gripper("above the wrench handle")
    # If the gripper isn't around the wrench handle, put it around the wrench
    # handle.
    if check("the robot's gripper is not around the wrench handle and the robot's gripper is open"):
        robot.move_gripper("near the wrench handle", close_gripper=True)
    # If the gripper is around the wrench handle and closed, we can probably pull
    # the wrench off the peg by just pulling the gripper up.
    if check("the robot's gripper is around the wrench handle and the robot's gripper is closed"):
        robot.move_gripper("above the peg")