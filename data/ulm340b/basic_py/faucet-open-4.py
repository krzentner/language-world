
    if check("the robot's gripper is not near the faucet"):
        robot.put("gripper below faucet")
    if check("the robot's gripper is near the faucet"):
        robot.turn("faucet left")

# pick: pick up the puck
def pick(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")

# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near the faucet"):
        robot.put("gripper below faucet")
    if check("the robot's gripper is near the faucet"):
        robot.turn("faucet right")

# sweep: sweep the puck into the goal
def sweep(robot):
    if check("the robot's gripper is not around the puck"):
        robot.put("gripper around puck")
    if check("the robot's gripper is around the puck and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.sweep("the puck to the goal")

# slider-close: close the slider
def slider_close(robot):
    if check("the robot's gripper is not vertically aligned with the slider handle"):
        robot.put("gripper above slider handle")
    if check("the robot's gripper is vertically aligned with the slider handle"):
        robot.move("gripper right")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not forward aligned with door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# peg-unplug-side: grab the peg and unplug it from the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is