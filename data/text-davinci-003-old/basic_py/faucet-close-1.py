
    if check("the robot's gripper is not near faucet handle"):
        robot.place("gripper near faucet handle")
    if check("the robot's gripper is near faucet handle and faucet handle is below the robot's gripper"):
        robot.grab("faucet handle")
    if check("the robot's gripper is near faucet handle and the robot's gripper is closed"):
        robot.twist("faucet right")