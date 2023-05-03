
    # Steps:
    #  1. Put gripper directly left of the faucet handle
    #  2. Rotate the handle to the left
    #  3. Open the faucet all the way
    # If the gripper is too far right, move it directly to the left of the
    # faucet handle.
    if check("the robot's gripper is not directly left of the faucet handle"):
        robot.move("gripper to left of faucet handle")
    # Grab the faucet handle with the gripper and rotate it to the left.
    # We don't need to grab the exit of the handle for this to work.
    if check("the robot's gripper is near the faucet handle"):
        robot.rotate("handle left")
    # If the handle is still moving, keep rotating it.
    if check("the handle is not in the open position"):
        robot.rotate("handle left")