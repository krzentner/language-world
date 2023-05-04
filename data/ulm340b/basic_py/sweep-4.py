
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.put("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.slide("to goal")

# toggle-switch-side: push the switch from side to side
def toggle_switch_side(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch and the switch is right of the robot's gripper"):
        robot.move("gripper to right of switch")
    if check("the switch is left of the robot's gripper"):
        robot.slide("switch to the right")
    if check("the robot's gripper is in front of switch and the switch is left of the robot's gripper"):
        robot.push("switch to the right")
    if check("the robot's gripper is not vertically aligned with switch and the robot's gripper is left of switch"):
        robot.move("gripper to left of switch")
    if check("the switch is right of the robot's gripper"):
        robot.slide("switch to the left")
    if check("the robot's gripper is in front of switch and the switch is right of the robot's gripper"):
        robot.push("switch to the left")

# turn-switch-vert: rotate the switch counterclockwise
def turn_switch_vert(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is not forward aligned with switch"):
        robot.put("gripper below switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.turn("switch counterclockwise")

# press: push the button down from the side
def press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not forward aligned with button"):
        robot.put