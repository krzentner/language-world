# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Move gripper to handle of faucet
    #  2. Use gripper to turn handle left
    # If the gripper is not near the faucet handle, move it there.
    if check("the robot's gripper is not near faucet handle"):
        robot.move("gripper to faucet handle")
    # If the gripper is near the handle, turn the handle left
    if check("the robot's gripper is near faucet handle"):
        robot.turn("faucet handle left")