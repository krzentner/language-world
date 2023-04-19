

# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper left of the faucet
    #  2. Move the gripper up to the faucet handle
    #  3. Push the faucet handle to the left
    # We need to move the robot's gripper to the left of the faucet handle
    # before we can turn it.
    if check("the robot's gripper is not left of faucet handle"):
        robot.move_gripper("left of the faucet handle")
    # If the faucet handle is left of the robot's gripper, move the gripper
    # up to the faucet handle.
    if check("the robot's gripper is left of the faucet handle and the robot's gripper is not above the faucet handle"):
        robot.move_gripper("above the faucet handle", close_gripper=True)
    # Now that the gripper is either above or close to the faucet handle, we can
    # push the handle to the left.
    if check("the robot's gripper is above the faucet handle or the robot's gripper is near the faucet handle"):
        robot.move_gripper("left of the faucet handle")