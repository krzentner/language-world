# Steps:
    #  1. Put gripper above faucet knob
    #  2. Grab onto the knob
    #  3. Turn the knob left to open the faucet
    # Align the gripper vertically with the faucet knob.
    if check("the robot's gripper is not vertically aligned with faucet knob"):
        robot.move_gripper("vertically aligned with the faucet knob")
    # Turn the knob left to open the faucet.
    if check("the robot's gripper is near the faucet knob and the faucet knob is not turned left"):
        robot.move_gripper("horizontally aligned with the faucet knob")
    # If the knob is turned partially left, keep turning the knob left until
    # we've fully opened the faucet.
    if check("the robot's gripper is near the faucet knob and the faucet knob is turned partially left"):
        robot.move_gripper("horizontally aligned with the faucet knob", close_gripper=True)

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet knob
    #  2. Grab onto the knob
    #  3. Turn the knob right to close the faucet
    # Align the gripper vertically with the faucet knob.
    if check("the robot's gripper is not vertically aligned with faucet knob"):
        robot.move_gripper("vertically aligned with the faucet knob")
    # Turn the knob right to close the faucet.
    if check("the robot's gripper is near the faucet knob and the faucet knob is not turned right"):
        robot.move_gripper("horizontally aligned with the faucet knob")
    # If the knob is turned partially left, keep turning the knob left until
    # we've fully opened the faucet.
    if check("the robot's gripper is near the faucet knob and the faucet knob is turned partially right"):
        robot.move_gripper("horizontally aligned with the faucet knob", close_gripper=True)