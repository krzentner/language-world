

Steps:
  1. Put gripper above faucet
  2. Turn faucet to the right

# faucet-close: turn the faucet to the right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet
    #  2. Turn faucet to the right
    # We need to put the gripper above the faucet before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.put("gripper above faucet")
    # Once the gripper is lined up above the faucet, we should be able to grab
    # the faucet by moving the gripper around it.
    if check("the robot's gripper is vertically aligned with faucet and the robot's gripper is not around faucet"):
        robot.put("gripper around faucet")
    # Try to turn the faucet to the right.
    if check("the robot's gripper is around faucet"):
        robot.turn("faucet to the right")