# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the handle left to open the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the handle, turn it left to open the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("left of the faucet handle")