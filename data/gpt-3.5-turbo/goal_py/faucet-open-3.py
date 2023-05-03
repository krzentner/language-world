# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    # 1. Put gripper around the faucet handle
    # 2. Grip the handle
    # 3. Turn the handle left to open the faucet
    # 4. Optional: adjust flow rate if desired
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the handle, close it to grip the handle.
    if check("the robot's gripper is around the faucet handle and the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Once the gripper has a good grip on the handle, turn it to the left to
    # open the faucet.
    if check("the robot's gripper is gripping the faucet handle and the faucet is not fully open"):
        robot.move_gripper("to the left of the faucet handle")
        # Optional: adjust flow rate if desired
        # ...
        
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    # 1. Put gripper around the faucet handle
    # 2. Grip the handle
    # 3. Turn the handle right to close the faucet
    # First, put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle")
    # Once the gripper is around the handle, close it to grip the handle.
    if check("the robot's gripper is around the faucet handle and the robot's gripper is open"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Once the gripper has a good grip on the handle, turn it to the right to
    # close the faucet.
    if check("the robot's gripper is gripping the faucet handle and the faucet is not fully closed"):
        robot.move_gripper("to the right of the faucet handle")