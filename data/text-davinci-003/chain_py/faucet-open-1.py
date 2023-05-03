
    # Steps:
    #  1. Put gripper above the faucet
    #  2. Drop gripper around the faucet
    #  3. Turn the faucet left
    # First, put the gripper above the faucet.
    if check("the robot's gripper is not vertically aligned with the faucet"):
        robot.put("gripper above faucet")
    # If the faucet is below the robot's gripper, try to grab it by moving the
    # gripper down around it.
    if check("faucet is below the robot's gripper and the robot's gripper is open and the robot's gripper is not around faucet"):
        robot.drop("gripper around faucet")
    # If the gripper is around the faucet, try to turn it.
    if check("the robot's gripper is around faucet"):
        robot.turn("faucet left")