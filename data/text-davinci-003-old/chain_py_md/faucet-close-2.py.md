

Steps:
  1. Put the gripper above the faucet
  2. Lower the gripper down around the faucet, making sure the gripper is not pressing down too hard
  3. Wind the faucet to the right, making sure to not exert too much pressure
  4. Check that the faucet is in the closed position

Robot Code:
```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put the gripper above the faucet
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.put("gripper above faucet")
    #  2. Lower the gripper down around the faucet, making sure the gripper is not pressing down too hard
    if check("the robot's gripper is not around faucet and the robot's gripper is open"):
        robot.grab("faucet")
    # 3. Wind the faucet to the right, making sure to not exert too much pressure
    if check("the robot's gripper is around faucet"):
        robot.wind("faucet right")
    #  4. Check that the faucet is in the closed position
    if check("the faucet is not fully closed"):
        robot.check("faucet closed")
```