
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.put("gripper above faucet")
    if check("the robot's gripper is forward aligned with faucet"):
        robot.turn("faucet left")