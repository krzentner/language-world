# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper near the faucet handle
    #  2. Turn the faucet left
    # We need to put the gripper near the faucet handle before we can turn it.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("near the faucet handle")
    # Once the gripper is near the faucet handle, we can turn it left.
    if check("the robot's gripper is near the faucet handle"):
        robot.move_gripper("turning the faucet left")