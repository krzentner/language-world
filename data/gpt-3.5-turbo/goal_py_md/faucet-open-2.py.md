# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    # 1. Position the gripper just above the faucet handle
    # 2. Grab the handle
    # 3. Turn the handle left to open the faucet
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle", close_gripper=True)
    # Once the gripper is positioned above the handle, grab it.
    if check("the robot's gripper is around the faucet handle and the robot's gripper is closed"):
        robot.move_gripper("left of the faucet handle")
    # Once the gripper is around the handle, turn it left to open the faucet.
    if check("the robot's gripper is almost vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle", close_gripper=False)