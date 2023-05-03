# Steps:
    #  1. Put gripper around faucet handle
    #  2. Turn the handle left
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # If the handle isn't turned left yet, turn it left.
    if check("the faucet handle is not turned left"):
        robot.turn("handle left")