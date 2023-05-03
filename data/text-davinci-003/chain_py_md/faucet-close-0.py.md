

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn the faucet to the right
    # First, put the gripper roughly above the faucet handle, so that we don't 
    # bump it while trying to grab it.
    if check("the robot's gripper is not above the faucet handle"):
        robot.place("gripper above faucet handle")
    # If the gripper isn't around the faucet handle, put it around the faucet handle.
    if check("the robot's gripper is not around faucet handle and the robot's gripper is open"):
        robot.drop("gripper around faucet handle")
    # If the gripper is near the faucet handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near faucet handle and the robot's gripper is open"):
        robot.close("gripper around faucet handle")
    # We closed the gripper, and the faucet handle is still near the gripper, so 
    # maybe we grabbed it. Try to turn the faucet to the right.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around faucet handle and the robot's gripper is closed"):
        robot.turn("faucet to the right")