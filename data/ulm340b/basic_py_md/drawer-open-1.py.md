

The first three statements should check to make sure the robot's gripper is not left of the drawer handle, not right of the drawer handle, and not near the drawer handle. If so, tell the robot to move its gripper to the drawer handle. The next statement should check to make sure the robot's gripper is near the drawer handle. If so, tell the robot to grab the drawer handle. Finally, the robot should check to make sure it's near the drawer handle, and then tell the robot to pull the drawer open.

In our study, we also collected demonstrations from many other tasks for a wide variety of robots. You can help by writing code to control those robots as well. Just copy and paste these blocks into the main text box.

# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not left of the drawer handle and the robot's gripper is not right of the drawer handle and the robot's gripper is not near the drawer handle"):
        robot.move("gripper to drawer handle")
    if check("the robot's gripper is near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with the drawer handle"):
        robot.pull("drawer open")

# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg")