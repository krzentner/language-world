
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# button-press-topdown-left: push the button down from above from the left
def button_press_topdown_left(robot):
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above button and the robot's gripper is not vertically aligned with button"):
        robot.push("gripper into button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button down")

# button-press-topdown-left-wall: push the button down from above from the left, with a short wall in the way
def button_press_topdown_left_wall(robot):
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above button and the robot's gripper is not vertically aligned with button"):
        robot.push("gripper into button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button down")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button down")

# button-press-side-right: push the button from the side from the right
def button_press_side_right(robot):
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above button and the robot's gripper is not vertically aligned with button"):
        robot.push("gripper into button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button down")

# button-press-side-right-wall: push the button from the side from the right, with a short wall in the way
def button_press_side