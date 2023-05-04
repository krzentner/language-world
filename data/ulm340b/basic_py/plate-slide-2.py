
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate"):
        robot.push("the plate to the goal")

# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle and the robot's gripper is left of the door handle"):
        robot.place("the gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("the gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.push("door closed")

# window-open: slide the window open to the left
def window_open(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# window-close: slide the window closed to the right
def window_close(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is left of button"):
        robot.place("the