

if check("the robot's gripper is not forward aligned with the faucet handle"):
    robot.put("gripper near to faucet handle")
if check("the robot's gripper is forward aligned with the faucet handle"):
    robot.grab("faucet handle")
if check("the robot's gripper is around the faucet handle"):
    robot.turn("anti-clockwise to open the faucet")