

if check("the robot's gripper is not vertically aligned with the faucet handle"):
    robot.put("gripper above faucet handle")
if check("the robot's gripper is vertically aligned with the faucet handle and the robot's gripper is not around faucet handle"):
    robot.put("gripper around faucet handle")
if check("the robot's gripper is around faucet handle"):
    robot.turn("faucet left")