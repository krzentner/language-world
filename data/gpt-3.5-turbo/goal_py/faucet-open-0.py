# Steps:
    #  1. Put hand on faucet handle
    #  2. Turn the handle left to open the faucet
    # To turn on the faucet, we need to grip the handle and turn it left.
    # First, put the robot's hand on the faucet handle.
    if check("the robot's hand is not on the faucet handle"):
        robot.move_hand("to the faucet handle")
    # If the hand is on the handle, turn it left to open the faucet.
    if check("the robot's hand is on the faucet handle"):
        robot.rotate_hand("left")