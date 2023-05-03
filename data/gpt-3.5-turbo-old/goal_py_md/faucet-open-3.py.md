# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put the gripper to the right side of the faucet handle
    #  2. Apply pressure to the handle and turn left
    #  3. Keep turning left until the water starts flowing
    # Move the gripper right of the faucet handle
    if check("the robot's gripper is not right of the faucet handle"):
        robot.move_gripper("right of the faucet handle")
    # Apply pressure to the handle and turn left
    if check("the robot's gripper is right of the faucet handle and the robot's gripper is not grabbing the handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
        robot.press_gripper()
        robot.turn_gripper(angle=-90)
    # Keep turning left until the water starts flowing
    if check("the water is not flowing"):
        robot.turn_gripper(angle=-90)