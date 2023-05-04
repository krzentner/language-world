
    if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.put("gripper into button")
    if check("the robot's gripper is near button and the button is not pressed"):
        robot.push("button down")

# peg-unstack: move the first of two stacked pegs from one slot to another
def peg_unstack(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("the gripper above the peg")
    if check("the robot's gripper is vertically aligned with peg"):
        robot.lift("the peg")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("the gripper")
    if check("the robot's gripper is near the peg and the robot's gripper is closed"):
        robot.hold("the peg at goal")

# button-press-side: push the button down from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.put("gripper into button")
    if check("the robot's gripper is near button and the button is not pressed"):
        robot.push("button down")

# drawer-close-side: push the drawer close from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not near drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is near drawer handle"):
        robot.push("drawer closed")

# valve-open: push the valve open
def valve_open(robot):
    if check("the robot's gripper is not above the valve and the robot's gripper is not vertically aligned