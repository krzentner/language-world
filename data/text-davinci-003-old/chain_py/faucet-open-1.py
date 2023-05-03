
    # Steps:
    #  1. Put the gripper on the left side of the faucet handle
    #  2. Move the faucet handle to the left
    # Because there are several directions we might be able to move the faucet
    # handle, we should start by lining up the gripper to the left of the faucet
    # handle.
    if check("the robot's gripper is not left of faucet handle"):
        robot.move("gripper to left of faucet handle")
    # If the gripper is lined up to the left of the faucet handle, just start
    # turning the faucet handle to the left.
    if check("the robot's gripper is left of faucet handle"):
        robot.turn("faucet handle left")