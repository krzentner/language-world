# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Move the gripper to the faucet handle
    #  2. Turn the faucet left
    # If the handle is to the right of the gripper and the gripper is not near
    # the handle, move the gripper to the handle.
    if check("the faucet handle is right of the robot's gripper and the robot's gripper is not near the faucet handle"):
        robot.move("gripper to right of faucet handle")
    # If the gripper is near the handle, we can probably turn the faucet now by
    # moving the gripper left.
    if check("the robot's gripper is near the faucet handle"):
        robot.turn("faucet left")