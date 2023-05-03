if check("the robot's gripper is not almost vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is almost vertically aligned with the faucet handle and the robot's gripper is around faucet handle"):
        robot.rotate("faucet handle right")
    if check("the faucet handle is pointing to the right"):
        robot.rotate("faucet handle right more")

# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not almost vertically aligned with the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is almost vertically aligned with the faucet handle and the robot's gripper is around faucet handle"):
        robot.rotate("faucet handle left")
    if check("the faucet handle is pointing to the left"):
        robot.rotate("faucet handle left more")