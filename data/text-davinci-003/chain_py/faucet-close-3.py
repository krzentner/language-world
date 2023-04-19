
    # Steps:
    #  1. Put gripper above the faucet
    #  2. Drop the gripper around the faucet
    #  3. Rotate the faucet right
    # We put the gripper above the faucet.
    if check("the robot's gripper is not above the faucet"):
        robot.put("gripper above faucet")
    # If the gripper is not yet around the faucet, try to grab it by putting the
    # gripper around the faucet.
    # We don't need to worry about the direction since we can just spin it.
    if check("the robot's gripper is not around faucet and the robot's gripper is open"):
        robot.put("gripper around faucet")
    # Once the faucet is lined up with the gripper, we can start rotating it.
    if check("the robot's gripper is around faucet and the robot's gripper is closed"):
        robot.rotate("faucet right")