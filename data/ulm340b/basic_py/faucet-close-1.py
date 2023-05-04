
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.close("faucet")

# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is vertically aligned with faucet handle"):
        robot.open("faucet")

# button-press-left: push the button to the left
def button_press_left(robot):
    if check("the robot's gripper is not left aligned with button and the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's gripper is near button"):
        robot.push("button to the left")

# button-press-right: push the button to the right
def button_press_right(robot):
    if check("the robot's gripper is not right aligned with button and the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's gripper is near button"):
        robot.push("button to the right")

# button-press-topleft: push the button down from top left
def button_press_topleft(robot):
    if check("the robot's gripper is not forward aligned with button and the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's gripper is near button"):
        robot.push("button down")

# button-press-topright: push the button down from top right
def button_press_topright(robot):
    if check("the robot's gripper is not forward aligned with button and the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's grip