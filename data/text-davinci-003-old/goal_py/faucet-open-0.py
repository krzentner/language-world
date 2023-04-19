
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the faucet handle left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Now the faucet handle is grabbed, turn it left to open the faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("left of the faucet handle")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the faucet handle right
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the faucet handle, turn it right to close the
    # faucet.
    if check("the robot's gripper is around faucet handle"):
        robot.move_gripper("right of the faucet handle")