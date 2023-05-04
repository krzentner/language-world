
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("handle downward")

# peg-unstack-side: grab the peg and move it to the target location
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with target location"):
        robot.align("peg to target location")
    if check("peg is horizontally aligned with target location"):
        robot.unstack("peg at goal")

# button-press: press the button sideways
def button_press(robot):
    if check("the robot's gripper is not near button"):
        robot.grab("button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button sideways")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# switch-press: push down the switch
def switch_press(robot):
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.put("gripper above switch")
    if check("the robot's gripper is vertically aligned with switch"):
        robot.push("switch downward")

# door-open-with-key: insert the key into the door and twist it sideways
def door_open_with_key(robot):
    if check("the robot's gripper is not vertically aligned with door keyhole"):
        robot.put("gripper above door keyhole")
    if check("the robot's gripper is vertically aligned with door keyhole and the key is not aligned with door keyhole"):
        robot.align("key with door keyhole")
    if check("the key is aligned with door keyhole and the key