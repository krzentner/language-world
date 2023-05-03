

If check("the robot's gripper is not vertically aligned with the faucet handle"):
    robot.put("gripper above faucet handle")
if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not near faucet handle"):
    robot.grab("faucet handle")
if check("the robot's gripper is near the faucet handle"):
    robot.turn("faucet left")