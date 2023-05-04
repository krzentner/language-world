
    # Steps:
    #  1. Put gripper around faucet
    #  2. Turn faucet left
    #  3. Keep turning faucet left
    # If the gripper is not around the faucet, put it there.
    if check("the robot's gripper is not around the faucet"):
        robot.move_gripper("around the faucet")
    # If the gripper is around the faucet, start turning it.
    if check("the robot's gripper is around the faucet"):
        robot.rotate_gripper("clockwise around the axis through the faucet's center and pointing down")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet
    #  2. Turn faucet right
    #  3. Keep turning faucet right
    # If the gripper is not around the faucet, put it there.
    if check("the robot's gripper is not around the faucet"):
        robot.move_gripper("around the faucet")
    # If the gripper is around the faucet, start turning it.
    if check("the robot's gripper is around the faucet"):
        robot.rotate_gripper("counterclockwise around the axis through the faucet's center and pointing down")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper around door handle
    #  2. Push door closed
    # If the gripper is not around the door handle, put it there.
    if check("the robot's gripper is not around door handle"):
        robot.move_gripper("around door handle")
    # If the gripper is around the door handle, start pushing the door closed.
    if check("the robot's gripper is around door handle"):
        robot.rotate_gripper("clockwise around the axis through door handle's center and pointing up")

# peg-unstack: pick the top peg off the top of the tower
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the top peg
    #  2. Grab the top peg
    #  3. Lift the top peg off of the stack
    # First, put the gripper above the top peg.