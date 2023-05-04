
    # Steps:
    #  1. Put the gripper around the faucet handle
    #  2. Turn the faucet open
    # If the gripper is not near the faucet handle, move it there.
    if check("the robot's gripper is not near faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # If the gripper is around the faucet handle, turn the faucet.
    if check("the robot's gripper is around faucet handle and the robot's gripper is above the faucet handle"):
        robot.move_gripper("horizontally aligned with faucet handle")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put the gripper around the faucet handle
    #  2. Turn the faucet closed
    # If the gripper is not near the faucet handle, move it there.
    if check("the robot's gripper is not near faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around the faucet handle")
    # If the gripper is around the faucet handle, turn the faucet.
    if check("the robot's gripper is around faucet handle and the robot's gripper is above the faucet handle"):
        robot.move_gripper("vertically aligned with faucet handle")

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper in front of peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg forwards into the hole
    # First, put the gripper in front of the peg, so that we can put the gripper
    # around the peg.
    if check("the robot's gripper is not in front of peg and the robot's gripper is not forward aligned with peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the robot's gripper is forward aligned with the peg but not around it,
    # we should move the gripper around the peg.
    # The robot's gripper is forward aligned with the peg but not