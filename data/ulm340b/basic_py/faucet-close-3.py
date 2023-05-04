
    if check("the robot's gripper is left of the faucet"):
        robot.slide("gripper to right of faucet")
    if check("the robot's gripper is vertically aligned with the faucet"):
        robot.turn("faucet right")

# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is right of the faucet"):
        robot.move("gripper to left of faucet")
    if check("the robot's gripper is vertically aligned with the faucet"):
        robot.turn("faucet left")

# switch-off: turn the switch off
def switch_off(robot):
    if check("the switch is left of the robot's gripper"):
        robot.slide("gripper to right of switch")
    if check("the robot's gripper is vertically aligned with the switch"):
        robot.turn("switch left")

# switch-on: turn the switch on
def switch_on(robot):
    if check("the switch is right of the robot's gripper"):
        robot.move("gripper to left of switch")
    if check("the robot's gripper is vertically aligned with the switch"):
        robot.turn("switch right")

# peg-unplug-side: pull the peg out of the hole
def peg_unplug_side(robot):
    if check("the robot's gripper is not horizontally aligned with the peg"):
        robot.align("gripper with peg")
    if check("peg is in front of the robot's gripper"):
        robot.pull("peg to right")

# pick-place-with-camera: pick up the puck and hold it at the target location, using a camera
def pick_place_with_camera(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")
