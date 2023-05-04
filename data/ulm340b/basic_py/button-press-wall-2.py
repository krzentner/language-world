
    if check("the button is not horizontally aligned with the robot's gripper"):
        robot.put("gripper at button")
    if check("the button is horizontally aligned with the robot's gripper and the button is not around the robot's gripper"):
        robot.grab("button")
    if check("the button is around the robot's gripper"):
        robot.push("button")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and button is not forward aligned with the robot's gripper"):
        robot.grab("button")
    if check("button is forward aligned with the robot's gripper"):
        robot.push("button")

# turn-valve: rotate the valve in a clockwise fashion
def turn_valve(robot):
    if check("the robot's gripper is not vertically aligned with valve and the robot's gripper is not near valve"):
        robot.put("gripper above valve")
    if check("the robot's gripper is vertically aligned with valve"):
        robot.grab("valve")
    if check("the robot's gripper is near valve and the robot's gripper is vertically aligned with valve"):
        robot.twist("valve")

# door-toggle: slide the toggle down to open the door
def door_toggle(robot):
    if check("the robot's gripper is not vertically aligned with the toggle"):
        robot.put("gripper above the toggle")
    if check("the robot's gripper is vertically aligned with the toggle"):
        robot.slide("the toggle down")

# drawer-close-soft: push the drawer closed slowly
def drawer_close_soft(robot):
    if check("the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed slowly")

# peg-unplug-side: pull the peg out of the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not near peg and peg is not vertically aligned with the robot's gripper"):
        robot.move