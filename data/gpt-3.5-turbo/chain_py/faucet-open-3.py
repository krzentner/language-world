# Steps:
    #   1. Put gripper around faucet handle
    #   2. Turn the faucet left
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.put("gripper around faucet handle")
    # Now that we've grabbed the handle, we can turn it left to open the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")