
    # Steps:
    #  1. Put gripper above the faucet knob
    #  2. Grab the faucet knob with gripper
    #  3. Start turning the faucet knob
    #  4. Turn the faucet knob harder
    # If the robot's gripper is not above the faucet knob, we should move the
    # gripper above the faucet knob.
    if check("the robot's gripper is not vertically aligned with the faucet knob"):
        robot.move_gripper("vertically aligned with the faucet knob")
    # If the robot's gripper is above the faucet knob, we can grab it by moving
    # the gripper around it.
    if check("the robot's gripper is vertically aligned with the faucet knob and the robot's gripper is not around the faucet knob"):
        robot.move_gripper("around the faucet knob", close_gripper=True)
    # Once the gripper is around the knob, start turning it to the left.
    if check("the robot's gripper is around the faucet knob"):
        robot.move_gripper("left of the faucet knob")
    # If the faucet is almost open, it probably won't open all the way with
    # gentle turning, push harder and hold for a bit to make sure it's open.
    if check("the faucet knob is not left of the robot's gripper and the faucet knob is not straight up"):
        robot.move_gripper("straight up")