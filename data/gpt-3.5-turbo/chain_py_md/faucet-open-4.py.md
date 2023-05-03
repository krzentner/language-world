# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put the gripper on the faucet handle
    #  2. Grab the faucet handle
    #  3. Turn the faucet to the left until it stops
    # Put the gripper on the faucet handle.
    if check("the robot's gripper is not on the faucet handle"):
        robot.move("gripper to faucet handle")
    # If the gripper is not around the faucet handle, grab it.
    if check("the robot's gripper is on the faucet handle and the gripper is not around the handle"):
        robot.grab("faucet handle")
    # Keep turning the handle to the left until it is fully turned (stopped).
    if check("the robot's gripper is around the faucet handle and the faucet is not fully turned left"):
        robot.turn("faucet left")