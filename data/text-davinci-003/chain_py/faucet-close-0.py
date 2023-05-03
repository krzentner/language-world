
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Line the gripper up with the handle
    #  3. Turn the handle right to close faucet
    # We need to put the gripper above the faucet handle before we can turn it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the faucet handle and the robot's gripper is open"):
        robot.put("gripper around faucet handle")
    # As long as the gripper is still mostly around the faucet handle and not
    # close to it, turn the handle right.
    if check("the robot's gripper is almost closed around the faucet handle and the faucet handle is not close to right"):
        robot.turn("faucet right")