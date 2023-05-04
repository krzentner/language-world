

"""

# Your code here!
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not near the plate and the robot's gripper is not forward aligned with the plate"):
        robot.slide("the plate to robot's gripper")
    if check("the robot's gripper is forward aligned with the plate"):
        robot.push("the plate into the goal")
    if check("the plate is near the goal"):
        robot.slide("the plate into goal")

# End your code here!

# This code is for your reference. It can be edited, but it will be overridden when running the experiments.


def check(condition):
    if eval(condition):
        return True
    return False


def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")


def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")


def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")


def peg_insert_side(