
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.place("gripper above faucet")
    if check("the robot's gripper is above faucet and the robot's gripper is not forward aligned with faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is forward aligned with faucet and the robot's gripper is not horizontally aligned with faucet"):
        robot.move("gripper to the right around faucet")
    if check("the robot's gripper is horizontally aligned with faucet and the robot's gripper is not rotated around faucet"):
        robot.push("faucet handle right")

# tap-close: turn the faucet right
def tap_close(robot):
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.place("gripper above faucet")
    if check("the robot's gripper is above faucet and the robot's gripper is not forward aligned with faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is forward aligned with faucet and the robot's gripper is not horizontally aligned with faucet"):
        robot.move("gripper to the right around faucet")
    if check("the robot's gripper is horizontally aligned with faucet and the robot's gripper is not rotated around faucet"):
        robot.push("faucet handle right")

# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.place("gripper above faucet")
    if check("the robot's gripper is above faucet and the robot's gripper is not forward aligned with faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is forward aligned with faucet and the robot's gripper is not horizontally aligned with faucet"):
        robot.move("gripper to the left around faucet")
    if check("the robot's gripper is horizontally aligned with faucet and the robot's gripper is not rotated around faucet"):
        robot.push("faucet handle left")

# tap-open: turn the faucet left
def tap_open(robot):
    if check("the robot's gripper is not vertically aligned with faucet"):
        robot.place("gripper above faucet")
    if check("the robot's gripper is above faucet and the robot's gripper is not