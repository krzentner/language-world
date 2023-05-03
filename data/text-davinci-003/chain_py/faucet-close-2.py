
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Grab the faucet handle
    #  4. Rotate the faucet right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # If we can move the gripper around the faucet handle all the way and the
    # gripper isn't in a good grabbing position, grab the faucet handle.
    # We just need to grab an edge with the gripper to twist the faucet.
    if check("the robot's gripper is around faucet handle and the robot's gripper is not in a good grabbing position"):
        robot.grab("faucet handle")
    # Once the gripper is grabbing the faucet handle, rotate it right.
    if check("the robot's gripper is grabbing faucet handle"):
        robot.rotate("faucet right")