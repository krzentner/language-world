

'''

robot = RobotWorld()
robot.initialize()
def check(condition_text):
    return eval(condition_text)

def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")

def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")

def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")

def window_close(robot):
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")

def window_open(robot):
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window