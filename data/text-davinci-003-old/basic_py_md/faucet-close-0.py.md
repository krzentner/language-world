

if check("the robot's gripper is not near of the faucet handle"):
    robot.reach("gripper near faucet handle")
if check("the robot's gripper is not aligned with the faucet handle"):
    robot.put("gripper around faucet handle")
if check("the robot's gripper is around faucet handle and the faucet is not in closed position"):
    robot.turn("faucet right")