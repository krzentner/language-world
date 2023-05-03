
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the handle
    #  3. Turn the handle to the right
    # As long as the gripper isn't lined up with the faucet handle, move it
    # above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is still above the handle, grab the handle with the
    # gripper.
    if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # If the handle has been grabbed, rotate it clockwise to close the faucet.
    if check("the robot's gripper is around the faucet handle"):
        robot.rotate("handle right")