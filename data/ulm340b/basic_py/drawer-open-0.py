
    if check("the robot's gripper is not near drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with the hole"):
        robot.put("peg above hole")
    if check("the robot's gripper is vertically aligned with the hole and peg is vertically aligned with hole"):
        robot.insert("peg into hole")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")

# button-press-side: press the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not left of the button"):
        robot.move("gripper to left of button")
    if check("the robot's gripper is near the button"):
        robot.press("button left")

def test_task(robot):
    robot.test_task()








































































































































































