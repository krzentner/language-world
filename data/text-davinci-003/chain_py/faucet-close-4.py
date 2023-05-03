
    # Steps:
    #  1. Put gripper on top of the faucet
    #  2. Turn the faucet right
    # Put the gripper on the faucet.
    if check("the robot's gripper is not vertically aligned with the faucet"):
        robot.put("gripper above faucet")
    # If the gripper is still lined up, turn the faucet right to close it.
    if check("the robot's gripper is vertically aligned with the faucet"):
        robot.turn("faucet right")