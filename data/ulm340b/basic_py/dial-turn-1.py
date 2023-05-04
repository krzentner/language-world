
    if check("the robot's gripper is not almost vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is almost vertically aligned with the dial and the robot's gripper is open"):
        robot.put("gripper around dial")
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is near the dial"):
        robot.twist("dial to goal")

# toggle-switch-on-topdown: push the toggle switch from above
def toggle_switch_on_topdown(robot):
    if check("the robot's gripper is not vertically aligned with switch and the robot's gripper is above switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.push("switch")

# toggle-switch-off-topdown: push the toggle switch from above
def toggle_switch_off_topdown(robot):
    if check("the robot's gripper is not vertically aligned with switch and the robot's gripper is above switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.pull("switch away")

# toggle-switch-on-side: push the toggle switch from the side
def toggle_switch_on_side(robot):
    if check("the robot's gripper is not vertically aligned with switch and the robot's gripper is above switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.grab("switch")
    if check("the robot's gripper is near the switch"):
        robot.push("switch to on")

# toggle-switch-off-side: push the toggle switch from the side
def toggle_switch_off_side(robot):
    if check("the robot's gripper is not vertically aligned with switch and the robot's gripper is above switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.grab("switch")
    if check("the robot's gripper is near the switch"):
        robot.push("switch to off")

# box-close: grab the box lid and slide it towards you to close the box
def