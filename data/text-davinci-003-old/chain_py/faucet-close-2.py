
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Push down on the faucet handle
    #  3. Turn the faucet right
    # Find where the faucet handle is and proceed to grab it.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Now that the gripper is around the faucet handle, push down on it.
    if check("the robot's gripper is around the faucet handle and the faucet handle is not pushed down"):
        robot.push("down on faucet handle")
    # If the faucet handle is pushed down and the robot's gripper is still
    # around, turn it right.
    if check("the robot's gripper is around the faucet handle and the faucet handle is pushed down"):
        robot.turn("right on faucet handle")