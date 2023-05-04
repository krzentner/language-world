
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above the handle and the handle is not vertically aligned with the gripper"):
        robot.push("gripper down on handle")
    if check("the handle is vertically aligned with the gripper"):
        robot.press("handle")

# light-switch: flip the light switch
def light_switch(robot):
    if check("the robot's gripper is not around the light switch"):
        robot.push("the gripper around the light switch")
    if check("the robot's gripper is around the light switch and the light switch is not horizontally aligned with the gripper"):
        robot.flip("the light switch")

# button-press: press the button
def button_press(robot):
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is almost vertically aligned with the button and the button is not vertically aligned with the robot's gripper"):
        robot.push("gripper down on button")
    if check("the button is vertically aligned with the gripper"):
        robot.press("button")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.close("door")

# toggle-switch: toggle the toggle switch
def toggle_switch(robot):
    if check("the robot's gripper is not almost vertically aligned with toggle switch"):
        robot.push("gripper above toggle switch")
    if check("the robot's gripper is above toggle switch and the toggle switch is not vertically aligned with the robot's gripper"):
        robot.put("gripper around toggle switch")
    if check("the toggle switch is vertically aligned with the gripper"):
        robot.toggle("toggle switch")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place