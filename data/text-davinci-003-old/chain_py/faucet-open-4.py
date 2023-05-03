
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper around the faucet handle
    #  3. Push faucet handle clockwise
    # We need to put the gripper above the faucet handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the faucet handle and the robot's gripper is open"):
        robot.grab("gripper around faucet handle")
    # As long as the gripper is still vertically aligned with the faucet handle,
    # it's being opened, so keep turning it clockwise.
    if check("the robot's gripper is vertically aligned with the faucet handle"):
        robot.turn("faucet handle clockwise")