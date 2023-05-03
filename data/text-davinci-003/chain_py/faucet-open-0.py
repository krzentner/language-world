
    # Steps:
    #  1. Put gripper over top of faucet handle
    #  2. Grab faucet handle
    #  3. Turn faucet left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.place("gripper over top of faucet handle")
    # If the gripper is lined up with the faucet handle but not near it, close 
    # the gripper to grab the faucet handle.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is open"):
        robot.close("gripper around faucet handle")
    # If the faucet handle is held by the gripper, turn the faucet to the left.
    if check("the robot's gripper is vertically aligned with the faucet handle and robot's gripper is closed"):
        robot.turn("left")