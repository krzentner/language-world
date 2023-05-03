

# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above faucet
    #  2. Drop gripper around faucet
    #  3. Turn the faucet left
    # First, put the gripper above the faucet.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.move_gripper("vertically aligned with the faucet")
    # If the gripper is not near the faucet handle, move the gripper lower
    # around the faucet handle.
    if check("the robot's gripper is not near faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, turn the faucet left.
    if check("the robot's gripper is near faucet handle"):
        robot.move_gripper("left of the faucet handle")