
    if check("the robot's gripper is not above dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above dial and the robot's gripper is not around dial"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around dial and the robot's gripper is not in front of dial"):
        robot.grab("dial")
    if check("the robot's gripper is in front of dial"):
        robot.turn("dial clockwise")

# handle-press: press down on the lever handle
def handle_press(robot):
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.press("handle down")

# drawer-close: pull the drawer closed
def drawer_close_v2(robot):
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.slide("drawer closed")

# slider-pull: pull the slider to the left
def slider_pull(robot):
    if check("the robot's gripper is not vertically aligned with the slider and the robot's gripper is not near slider"):
        robot.put("gripper above slider")
    if check("the robot's gripper is near slider"):
        robot.pull("slider left")
    if check("the robot's gripper is in front of slider"):
        robot.push("slider left harder")

# slider-push: push the slider to the right
def slider_push(robot):
    if check("the robot's gripper is not almost vertically aligned with slider and the robot's gripper is not near slider"):
        robot.put("gripper above slider")
    if check("the robot's gripper is near slider"):
        robot.push("slider right")
    if check("the robot's gripper is in front of slider"):
        robot.slide("slider right harder")

# light-switch: flip