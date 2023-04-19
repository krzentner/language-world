

If check("the robot's gripper is not vertically aligned with the faucet"):
    robot.put("gripper above faucet")
If check("the robot's gripper is vertically aligned with the faucet and the robot's gripper is not around the faucet"):
    robot.drop("gripper around faucet")
If check("the robot's gripper is around the faucet"):
    robot.turn("faucet left")