
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet left
    # First, put the gripper roughly above faucet handle, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle")
    # If the gripper isn't around the faucet handle, put it around the faucet
    # handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.move_gripper("near the faucet handle", close_gripper=True)
    # Once the gripper has the faucet handle clasped, rotate the faucet counter-
    # clockwise to open it.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("counterclockwise", rotate_only=True)