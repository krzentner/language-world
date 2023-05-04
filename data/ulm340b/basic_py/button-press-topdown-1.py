
    if check("the robot's gripper is not almost above the button and the robot's gripper is below the button"):
        robot.move("gripper to almost above the button")
    if check("the robot's gripper is almost above the button"):
        robot.push("button into the button frame")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not almost near the door handle and the robot's gripper is not vertically aligned with the door handle"):
        robot.move("gripper to almost near the door handle")
    if check("the robot's gripper is almost near the door handle"):
        robot.push("door closed")

# slide-window-close: close the window with the handle to the right
def slide_window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# slide-drawer-open: open the drawer with the handle to the left
def slide_drawer_open(robot):
    if check("the drawer handle is left of the robot's gripper and the robot's gripper is not near the drawer handle"):
        robot.move("gripper to right of drawer handle")
    if check("the robot's gripper is near the drawer handle"):
        robot.slide("drawer left")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.pull("drawer left harder")

# slide-drawer-close: close the drawer with the handle to the left
def slide_drawer_close(robot):
    if check("the drawer handle is left of the robot's gripper and the robot's gripper is not near the drawer handle"):
        robot.move("gripper to right of drawer handle")
    if check("the robot's gripper is near the drawer handle"):
        robot.slide("drawer left")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer left harder")

# pull-door-open: open