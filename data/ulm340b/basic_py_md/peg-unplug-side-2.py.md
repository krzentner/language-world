
"""


def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")


def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if (
        check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle")
    ):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")


def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if (
        check(
            "the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"
        )
    ):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")


def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")


def window_open(robot):
    if (
        check(
            "the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"
        )
    ):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")


def window_close(robot):
    if (
        check("the window handle is right of the robot's grip