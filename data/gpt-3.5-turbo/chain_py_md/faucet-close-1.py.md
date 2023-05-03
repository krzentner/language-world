# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper near faucet handle
    #  2. Grab the handle
    #  3. Turn the handle to the right to close the faucet
    # Move the gripper near the faucet handle.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper near faucet handle")
    # Grab the handle if the gripper is lined up with it and not already around it.
    if check("the robot's gripper is aligned with the faucet handle and the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    # Keep turning the handle to the right until it's been closed.
    if check("the faucet is not closed"):
        robot.turn("faucet handle", "right")