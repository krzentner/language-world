
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.move("handle up to goal")

# handle-pull-side: pull the handle from the side
def handle_pull_side(robot):
    if check("the robot's gripper is not left of handle and the robot's gripper is not vertically aligned with handle"):
        robot.move("gripper to left of handle")
    if check("the robot's gripper is left of handle and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.move("handle right")

# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.move("handle down to goal")

# light-switch-off: flick the switch down
def light_switch_off(robot):
    if check("the robot's gripper is not below the light switch and the robot's gripper is not forward aligned with the light switch"):
        robot.put("gripper below light switch")
    if check("the robot's gripper is forward aligned with the light switch"):
        robot.flick("light switch down")

# light-switch-on: flick the switch up
def light_switch_on(robot):
    if check("the robot's gripper is not above light switch"):
        robot.place("gripper above light switch")
    if check("the robot's gripper is above light switch and the robot's gripper is not vertically aligned with light switch"):
        robot.put("gripper vertically aligned with light switch")
    if check("the robot's gripper is not forward aligned with light switch and the robot