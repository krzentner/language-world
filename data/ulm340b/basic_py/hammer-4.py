
    if check("the hammer is not vertically aligned with nail and the hammer is not aligned with nail"):
        robot.place("hammer at nail")
    if check("the hammer is vertically aligned with nail"):
        robot.drop("hammer")

# handle-press: press down on the handle
def handle_press(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is near handle"):
        robot.push("down on handle")

# door-close: push the door close
def door_close(robot):
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# pull-drawer: pull the drawer open
def pull_drawer(robot):
    if check("the robot's gripper is not above drawer handle"):
        robot.place("gripper above drawer handle")
    if check("the robot's gripper is near drawer handle"):
        robot.pull("drawer open")

# slide-window: slide the window open
def slide_window(robot):
    if check("the robot's gripper is not above window handle"):
        robot.place("gripper above window handle")
    if check("the robot's gripper is near window handle"):
        robot.slide("window open")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.place("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.pull("door open")

# reach: reach to the