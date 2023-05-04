
    if check("the drawer is open and the drawer handle is not near the robot's gripper"):
        robot.put("gripper around drawer handle")
    if check("the drawer handle is near the robot's gripper and the drawer handle is in front of the robot's gripper"):
        robot.push("the drawer closed")

# door-close: push the door close
def door_close(robot):
    if check("the door is open and the door handle is not near the robot's gripper"):
        robot.put("gripper around door handle")
    if check("the door handle is near the robot's gripper and the door handle is in front of the robot's gripper"):
        robot.push("the door closed")

# button-press-side: push the button sideways
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button to the right")

# button-press-bottomup: push the button up from below
def button_press_bottomup(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("up on button")

# switch-toggle-left: push the toggle switch leftwards
def switch_toggle_left(robot):
    if check("the robot's gripper is not vertically aligned with switch handle"):
        robot.put("gripper above switch handle")
    if check("the robot's gripper is vertically aligned with switch handle"):
        robot.push("switch to the left")

# switch-toggle-right: push the toggle switch rightwards
def switch_toggle_right(robot):
    if check("the robot's gripper is not vertically aligned with switch handle"):
        robot.put("gripper above switch handle")
    if check("the robot's gripper is vertically aligned with switch handle"):
        robot.push("switch to the right")

# door-toggle-left: push the toggle switch leftwards
def door_toggle_left(robot):
    if check("the robot's gripper is not vertically aligned with switch handle"):
        robot.put("gripper above switch handle")
