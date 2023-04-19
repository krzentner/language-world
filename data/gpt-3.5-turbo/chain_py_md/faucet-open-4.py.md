# faucet-open: turn the faucet left
# def faucet_open(robot):
    # Steps:
    #  1. Put gripper near the faucet handle
    #  2. Grab the faucet handle with the gripper
    #  3. Turn the handle left to open the faucet
    #  4. Turn the handle harder if the faucet isn't open yet
    # Move the robot's gripper close to the faucet handle from the side.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper near faucet handle")
    # Once the gripper is close, we can try to grab the handle.
    if check("the robot's gripper is near the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Now that the handle is grabbed, turning the robot's gripper left should
    # open the faucet.
    if check("the robot's gripper is around the faucet handle and the faucet is not open"):
        robot.turn("faucet handle left")
    # If the handle didn't turn enough to open the faucet, turn it harder until
    # it does.
    if check("the faucet is not open"):
        robot.turn("faucet handle harder")