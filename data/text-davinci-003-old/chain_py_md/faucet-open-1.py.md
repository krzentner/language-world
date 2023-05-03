

# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet handle
    #  2. Drop gripper to the faucet handle
    #  3. Turn the faucet to the left
    # First, put the gripper above the faucet handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # As long as the gripper is not wrapped around the handle, close the gripper
    # around the handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.drop("gripper around faucet handle")
    # As long as the gripper is still around the faucet handle, turn it to the
    # left.
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")