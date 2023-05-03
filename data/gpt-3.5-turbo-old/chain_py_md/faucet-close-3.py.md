# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    # 1. Put gripper around faucet
    # 2. Turn the faucet right
    # First, put the gripper around the faucet.
    if check("the robot's gripper is not around the faucet and the robot's gripper is open"):
        robot.drop("gripper around faucet")
    # Once the gripper is around the faucet, turn the faucet to the right.
    if check("the robot's gripper is around the faucet and the faucet handle is not in the right position"):
        robot.turn("faucet right")