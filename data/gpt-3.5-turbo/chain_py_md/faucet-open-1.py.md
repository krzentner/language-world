# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Move the gripper close to the faucet handle
    #  2. Grab the handle with the gripper
    #  3. Turn the handle left
    # First, we need to place the gripper near the faucet handle.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper near faucet handle")
    # Next, we need to grab the handle with the gripper.
    if check("the handle is not grabbed by the robot's gripper"):
        robot.grab("faucet handle")
    # Finally, we can turn the handle left to open the faucet.
    if check("the faucet handle is not turned left"):
        robot.turn("faucet handle left")