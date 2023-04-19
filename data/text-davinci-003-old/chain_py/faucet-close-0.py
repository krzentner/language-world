
    # Steps:
    #  1. Put gripper above the faucet
    #  2. Drop gripper around the faucet
    #  3. Turn the faucet to the right
    # First, put the gripper above the faucet.
    if check("the robot's gripper is not vertically aligned with the faucet"):
        robot.put("gripper above faucet")
    # If the gripper is almost lined up, closing it should line it up all the
    # way.
    if check("the robot's gripper is almost vertically aligned with the faucet and the robot's gripper is open"):
        robot.put("gripper around faucet")
    # As long as the gripper is still vertically aligned with the faucet, it's
    # being turned, so keep turning.
    if check("the robot's gripper is vertically aligned with the faucet"):
        robot.turn("faucet right")