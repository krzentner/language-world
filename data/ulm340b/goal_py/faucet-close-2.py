
    # Steps:
    #  1. Put gripper left of the faucet
    #  2. Start pushing against the faucet to close it
    #  3. Push the faucet closed harder
    # If the the faucet is right of the robot's gripper, we should move the
    # gripper near the faucet to start pushing
    if check("the robot's gripper is in front of the faucet"):
        robot.move_gripper("right of the faucet")
    # If the robot's gripper is near the faucet we can probably push it closed
    # now by moving the gripper right.
    if check("the faucet is right of the robot's gripper and the robot's gripper is not near the faucet"):
        robot.move_gripper("near the faucet")
    # If the robot's gripper is starting to be in front of the faucet, push
    # harder.
    if check("the robot's gripper is near the faucet and the robot's gripper is not in front of the faucet"):
        robot.move_gripper("in front of the faucet")

# turn-switch-off: turn the switch off
def turn_switch_off(robot):
    # Steps:
    #  1. Put gripper left of the switch
    #  2. Start pushing against the switch to turn it off
    #  3. Push the switch harder to turn it off
    # If the the switch is right of the robot's gripper, we should move the
    # gripper near the switch to start pushing
    if check("the robot's gripper is in front of the switch"):
        robot.move_gripper("right of the switch")
    # If the robot's gripper is near the switch we can probably push it closed
    # now by moving the gripper right.
    if check("the switch is right of the robot's gripper and the robot's gripper is not near the switch"):
        robot.move_gripper("near the switch")
    # If the robot's gripper is starting to be in front of the switch, push
    # harder.
    if check("the robot's gripper is near the switch"):
        robot.move_gripper("in front of the switch")

# switch-flip: flip the switch up
def switch_flip(robot):
 