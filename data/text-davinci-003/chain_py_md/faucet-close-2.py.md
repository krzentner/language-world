

Then add the following code:


    # Steps:
    #  1. Put gripper above the faucet
    #  2. Drop gripper around the faucet
    #  3. Turn the faucet to the right
    # We need to put the gripper above the faucet before we can grab it, because of the
    # angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.put("gripper above faucet")
    # Once the gripper is lined up above the faucet, we should be able to grab the
    # faucet by moving the gripper down and around it.
    if check("the robot's gripper is vertically aligned with faucet and the robot's gripper is not around faucet"):
        robot.drop("gripper around faucet")
    # Once the gripper is around the faucet, we can just turn the faucet to the
    # right.
    if check("the robot's gripper is around faucet"):
        robot.turn("faucet right")