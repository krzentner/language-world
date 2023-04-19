
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Grab faucet handle
    #  3. Turn faucet handle left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # When the gripper is vertically aligned with the faucet handle, grab it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Now that the gripper is around the faucet handle, turn it left.
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")