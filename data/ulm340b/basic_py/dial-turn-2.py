
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not near dial"):
        robot.grab("dial")
    if check("the robot's gripper is vertically aligned with dial"):
        robot.turn("dial")

# peg-unplug-side: hold the peg and remove it from the hole
def peg_unplug_side(robot):
    if check("the robot's gripper is not near peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is forward aligned with peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is horizontally aligned with peg and the robot's gripper is closed"):
        robot.pull("peg from hole")

# drawer-knob-pull: pull open the drawer by the knob
def drawer_knob_pull(robot):
    if check("the robot's gripper is not around the drawer knob"):
        robot.grab("drawer knob")
    if check("the robot's gripper is near the drawer knob"):
        robot.pull("drawer knob")

# peg-insert-vertical: grab the peg and insert it into the hole from above
def peg_insert_vertical(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# button-press-side: push the button sideways
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button sideways")

# button-press-topdown-side: push the button down from the side
def button_