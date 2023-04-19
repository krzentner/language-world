

if check("the robot's gripper is not near the faucet handle"):
    robot.move("gripper to faucet handle")
if check("the robot's gripper is near the faucet handle and the robot's gripper is not horizontally aligned with the faucet handle"):
    robot.align("gripper to faucet handle")
if check("the robot's gripper is horizontally aligned with the faucet handle and the robot's gripper is open"):
    robot.grab("faucet handle")
if check("the robot's gripper is around the faucet handle"):
    robot.turn("faucet left")