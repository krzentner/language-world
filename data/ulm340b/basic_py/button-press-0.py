
    if check("the robot's gripper is not near the button"):
        robot.grab("the button")
    if check("the robot's gripper is near the button"):
        robot.push("the button down")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("peg is below the robot's gripper and peg is not left of the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not above the door handle and the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# knob-turn-left: turn the knob to the left
def knob_turn_left(robot):
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with the knob and the robot's gripper is not around the knob"):
        robot.put("gripper around knob")
    if check("the robot's gripper is around the knob"):
        robot.turn("knob left")

# knob-turn-right: turn the knob to the right
def knob_turn_right(robot):
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.put("gripper above knob")
    if check("the robot's gripper is vertically aligned with the knob and the robot's gripper is not around the knob"):
        robot.put("gripper around knob")
    if