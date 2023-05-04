
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is near dial and the robot's gripper is not above dial"):
        robot.turn("dial right")

# valve-turn: turn the valve handle
def valve_turn(robot):
    if check("the robot's gripper is not vertically aligned with valve handle"):
        robot.put("gripper above valve handle")
    if check("the robot's gripper is vertically aligned with valve handle"):
        robot.put("gripper around valve handle")
    if check("the robot's gripper is around valve handle and the robot's gripper is above valve handle"):
        robot.turn("valve handle left")
    if check("the robot's gripper is around valve handle"):
        robot.pull("valve handle left")

# peg-insert-vertical: grab the peg and insert it into the hole from above
def peg_insert_vertical(robot):
    if check("the robot's gripper is not near the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is around the peg and the peg is not vertically aligned with hole"):
        robot.grab("peg")
    if check("the robot's gripper is near the peg and the peg is vertically aligned with hole"):
        robot.insert("peg into hole")

# drawer-close: push the drawer closed
def drawer_close(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's grip