
    # Steps:
    #  1. Put gripper near the faucet
    #  2. Start turning the faucet right
    #  3. Turn the faucet harder
    # If the gripper is not near the faucet, move it near the faucet.
    if check("the robot's gripper is not near the faucet"):
        robot.move_gripper("near the faucet")
    # If the gripper is near the faucet, start turning it right by moving the
    # gripper left
    if check("the robot's gripper is near the faucet"):
        robot.move_gripper("right of the faucet")
    # If the gripper is almost lined up with the faucet, we can turn it harder
    # by pushing the gripper left.
    if check("the robot's gripper is almost vertically aligned with the faucet"):
        robot.move_gripper("left of the faucet")