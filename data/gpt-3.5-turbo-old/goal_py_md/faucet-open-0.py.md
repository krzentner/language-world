# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    # 1. Put gripper near the left knob of the faucet
    # 2. Grab the knob with the gripper
    # 3. Turn the knob left to open the faucet
    # First, put the gripper near the left knob of the faucet
    if check("the robot's gripper is not near the left knob of the faucet"):
        robot.move_gripper("near the left knob of the faucet")
    # If the gripper is near the knob, grab it
    if check("the robot's gripper is near the left knob of the faucet and the robot's gripper is open"):
        robot.move_gripper("around the left knob of the faucet", close_gripper=True)
    # If the knob is grabbed, then turn it left until the faucet is fully open
    if check("the robot's gripper is around the left knob of the faucet"):
        robot.turn_gripper_left()