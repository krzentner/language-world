
    if check("the robot's gripper is not right of handle and the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("handle is left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("handle is forward aligned with the robot's gripper and handle is not vertically aligned with the robot's gripper"):
        robot.pull("handle up")

# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not left of drawer handle and the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("drawer handle is right of the robot's gripper and drawer handle is not forward aligned with the robot's gripper"):
        robot.grab("drawer handle")
    if check("drawer handle is forward aligned with the robot's gripper and drawer handle is not vertically aligned with the robot's gripper"):
        robot.push("drawer closed")

# handle-pull: pull up the handle from above
def handle_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with handle and the robot's gripper is not right of handle"):
        robot.put("gripper above handle")
    if check("handle is left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("handle is forward aligned with the robot's gripper and handle is not vertically aligned with the robot's gripper"):
        robot.pull("handle up")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button and button is not forward aligned with the robot's gripper"):
        robot.grab("button")
    if check("button is not horizontally aligned with the robot's gripper"):
        robot.push("button down")

# door-close: slide the door closed to the left
def door_close(robot):
    if check("the robot's gripper is not left of door handle and the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")