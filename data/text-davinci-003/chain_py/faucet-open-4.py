
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the faucet counterclockwise
    # Start by putting the gripper above the faucet handle
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # If the faucet handle isn't in front of the gripper, move the gripper to
    # the handle.
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not in front of the faucet handle"):
        robot.grab("faucet handle")
    # Once the gripper is in front of the faucet handle, hold it and turn it
    # counterclockwise.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.turn("counterclockwise")