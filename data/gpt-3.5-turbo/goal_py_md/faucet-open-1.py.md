# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    # 1. Put the gripper above the faucet handle
    # 2. Turn the faucet handle left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the robot's gripper is above the faucet handle but not around it, move
    # the gripper down and close the gripper around the faucet handle.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Rotate the gripper to the left to turn the faucet handle.
    if check("the faucet is not fully turned on"):
        robot.rotate_gripper("left")