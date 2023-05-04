
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is behind the window handle"):
        robot.push("window right harder")

# window-open-right: slide the window open to the right
def window_open_right(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is behind the window handle"):
        robot.push("window right harder")

# window-close-right: slide the window closed to the left
def window_close_right(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# button-press-left: push the button down from the left
def button_press_left(robot):
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.push("the gripper to the left of the button")
    if check("the robot's gripper is left of the button"):
        robot.push("down on button")

# door-unlock: turn the door knob
def door_unlock(robot):
    if check("the robot's gripper is not vertically aligned with the door knob"):
        robot.put("the