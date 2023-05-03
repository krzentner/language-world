
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around faucet handle"):
        robot.grab("faucet handle")
    if check("the robot's gripper is around faucet handle"):
        robot.turn("faucet left")

# shelf-lower: lower the shelf
def shelf_lower(robot):
    if check("the robot's gripper is not vertically aligned with shelf handle"):
        robot.put("gripper above shelf handle")
    if check("the robot's gripper is vertically aligned with shelf handle and the robot's gripper is not around shelf handle"):
        robot.grab("shelf handle")
    if check("the robot's gripper is around shelf handle and shelf is not lowered"):
        robot.pull("shelf down")