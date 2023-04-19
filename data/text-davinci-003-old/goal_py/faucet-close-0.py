
    # Steps:
    #  1. Put gripper left of the faucet
    #  2. Grab the faucet with the gripper
    #  3. Turn the faucet right
    # We need to line up the gripper with the faucet from the left.
    if check("the robot's gripper is not left of the faucet"):
        robot.move_gripper("left of the faucet")
    # Once the gripper is lined up with the faucet, grab the faucet in the
    # gripper.
    if check("the robot's gripper is left of the faucet"):
        robot.move_gripper("around the faucet", close_gripper=True)
    # Now that we have the faucet in the gripper, turn it right.
    if check("the robot's gripper is around the faucet"):
        robot.move_gripper("right of the faucet")