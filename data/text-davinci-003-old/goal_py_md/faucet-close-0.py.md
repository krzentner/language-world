

Steps:
1. Put gripper above faucet handle
2. Drop gripper around faucet handle
3. Turn the faucet handle to the right

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet handle to the right
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the faucet handle becomes left of the gripper, go back to putting the
    # gripper above the faucet handle.
    # Because the faucet handle is a long object, check if the gripper is lined
    # up with it from the front instead of around it.
    if check("faucet handle is not left of the robot's gripper and faucet handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the faucet handle", close_gripper=True)
    # As long the gripper is still mostly around the faucet handle, turn the
    # faucet handle to the right.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of the faucet handle")