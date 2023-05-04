
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.align("gripper with handle")
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("handle down")

# peg-insert-side-long: grab the peg and insert it into the hole from the side
def peg_insert_side_long(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the peg is not horizontally aligned with the hole"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# turn-switch-right: turn the switch to the right until horizontal
def turn_switch_right(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.turn("switch to right")

# pick: pick up the puck
def pick(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")

# peg-unstack-side-long: grab the peg and unstack it from the hole
def peg_unstack_side_long(robot):
    if check("the robot's gripper is not vertically aligned with the peg and the peg is not horizontally aligned with the hole"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.unstack("peg from hole")

# button-press-