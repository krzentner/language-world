
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the faucet handle left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above the faucet handle")
    # If the faucet handle is left of the gripper, go back to putting the
    # gripper above the faucet handle.
    # Because the faucet handle is a circular object, check if the gripper is
    # lined up with it from the front instead of around it.
    if check("the faucet handle is not left of the robot's gripper and the faucet handle is not forward aligned with the robot's gripper"):
        robot.grab("faucet handle")
    # If the gripper is forward aligned with the faucet handle and the faucet
    # handle is not turned, turn it left.
    if check("the robot's gripper is forward aligned with the faucet handle and the faucet handle is not turned"):
        robot.turn("faucet handle left")