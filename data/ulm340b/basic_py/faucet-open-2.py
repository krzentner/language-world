
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle"):
        robot.grab("handle")
    if check("the robot's gripper is near handle"):
        robot.turn("handle left")

# toggle-switch-on: pull the switch on
def toggle_switch_on(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is near switch and the robot's gripper is closed"):
        robot.grab("switch")
    if check("the robot's gripper is open"):
        robot.pull("switch on")

# toggle-switch-off: push the switch off
def toggle_switch_off(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is near switch and the robot's gripper is closed"):
        robot.grab("switch")
    if check("the robot's gripper is open"):
        robot.push("switch off")

# dial-turn: turn the dial to the right
def dial_turn(robot):
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.place("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial"):
        robot.turn("dial right")

# button-press: press the button in
def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.move("gripper towards button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")

# oven-pull-open: pull the oven open
def oven_pull_open(robot):
    if check("the robot's gripper is not above oven handle"):
        robot.put("gripper above oven handle")
    if check("the robot's gripper is above oven handle"):
        robot.pull("oven open")

# slide-window-closed: slide the window closed to the right
def slide_window_closed