```
# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    # 1. Put gripper below the faucet handle
    # 2. Lock gripper around the handle
    # 3. Rotate the handle right
    # 4. Check if rotation succeeded by checking if the water has stopped running
    # Move the gripper below the faucet handle.
    if check("the robot's gripper is not vertically aligned with the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # Grab the handle by closing the gripper around it.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("around the faucet handle", close_gripper=True)
    # Rotate the handle right to close it.
    if check("the robot's gripper is around the faucet handle"):
        robot.move_gripper("right of the faucet handle")
    # Check if the rotation succeeded by checking if the water has stopped running.
    if check("water is no longer running"):
        print("Faucet closed successfully.")
    else:
        print("Faucet did not close successfully. Please try again.")
```