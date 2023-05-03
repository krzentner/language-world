
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the faucet counter clockwise
    #  4. Turn the faucet harder
    # We need to put the gripper above and then capture the faucet handle to
    # start turning it. We don't need to be exact, since the faucet is a big
    # target.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # Once the gripper is above the faucet handle, it's almost lined up and we
    # can grab the handle.
    if check("the robot's gripper is nearly vertically aligned with the faucet handle and the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # If the gripper is still near the faucet handle, turn it counter-clockwise
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet counter clockwise")
    # If it's starting to open, turn it harder and faster until it's fully
    # open.
    if check("faucet is opening"):
        robot.turn("faucet harder")