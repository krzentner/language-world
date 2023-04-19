
    # Steps:
    #  1. Put gripper above the faucet
    #  2. Drop gripper around the faucet
    #  3. Rotate the faucet handle to the right
    # First, put the gripper roughly above the faucet handle.
    if check("the robot's gripper is not above faucet handle"):
        robot.put("gripper above faucet handle")
    # Once the gripper is above the faucet handle, closing it should make the
    # gripper around the handle.
    if check("the robot's gripper is above faucet handle and the robot's gripper is open"):
        robot.drop("gripper around faucet handle")
    # Now that the gripper has a hold on the handle, rotate it to the right.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet right")