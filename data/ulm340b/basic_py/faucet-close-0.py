
    if check("the robot's gripper is not forward aligned with faucet"):
        robot.grab("faucet handle")
    if check("the robot's gripper is forward aligned with faucet"):
        robot.rotate("faucet right")

# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not forward aligned with faucet"):
        robot.grab("faucet handle")
    if check("the robot's gripper is forward aligned with faucet"):
        robot.rotate("faucet left")

# door-close: pull the door close
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not forward aligned with button"):
        robot.grab("button")
    if check("the robot's gripper is not forward aligned with button"):
        robot.rotate("button inwards")

# pick-place-side: approach the puck from the side, pick it up, and hold it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not forward aligned with puck and the robot's gripper is not near puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is not left of puck and the robot's gripper is not forward aligned with puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.put("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.place("puck at goal")

# pick-place-side-v2: approach the puck from the side, pick it up, and hold it at the target location
def pick_place_side_v2(robot):
    if check("the robot's gripper is not