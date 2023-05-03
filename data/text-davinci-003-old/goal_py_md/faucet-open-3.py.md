

Steps:
1. Put gripper in front of faucet
2. Turn the faucet left

If the robot's gripper is not near the faucet, move the gripper near the faucet.
    if check("the robot's gripper is not near the faucet"):
        robot.move_gripper("near the faucet")

If the gripper is near the faucet, turn the faucet left.
    if check("the robot's gripper is near the faucet"):
        robot.move_gripper("forward aligned with the faucet")