
    if check("the drawer is open and the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("away from drawer")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the button is above the robot's gripper and the robot's gripper is right of the button"):
        robot.move("gripper to above the button")
    if check("the robot's gripper is above button and robot's gripper is not near button"):
        robot.move("gripper to button")
    if check("the robot's gripper is near the button"):
        robot.push("button forward")

# button-press-topdown-side: push the button from the side or above
def button_press_topdown_side(robot):
    if check("the button is above the robot's gripper and the robot's gripper is right of the button"):
        robot.move("gripper to above the button")
    if check("the robot's gripper is above button and robot's gripper is not near button"):
        robot.move("gripper to button")
    if check("the robot's gripper is near the button"):
        robot.push("button forward")

# drawer-open-side: pull the drawer open from the side
def drawer_open_side(robot):
    if check("the drawer handle is to the right of the robot's gripper and the robot's gripper is below drawer handle"):
        robot.move("gripper above drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")
    if check("the drawer is not open"):
        robot.pull("away from drawer harder")

# door-open-side: pull the door open from the side
def door_open_side(robot):
    if check("the door handle is to the right of the robot's gripper and the robot's gripper is below drawer handle"):
        robot.move("gripper above door handle")
    if check("the robot