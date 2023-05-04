
    if check("the robot's gripper is not forward aligned with dial"):
        robot.rotate("gripper around dial")
    if check("the robot's gripper is forward aligned with dial"):
        robot.rotate("dial to goal")

# handle-press-side: press down on the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not forward aligned with handle"):
        robot.align("gripper to handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.press("handle down")

# door-close: pull the door shut
def door_close(robot):
    if check("the robot's gripper is not forward aligned with door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# handle-pull: pull the handle toward the robot
def handle_pull(robot):
    if check("the robot's gripper is not near handle and the robot's gripper is not forward aligned with handle"):
        robot.grab("handle")
    if check("the robot's gripper is near handle"):
        robot.pull("handle toward robot")

# box-close: close the latch on the box
def box_close(robot):
    if check("the robot's gripper is not vertically aligned with latch and latch is not forward aligned with the robot's gripper"):
        robot.move("gripper to above the latch")
    if check("the robot's gripper is vertically aligned with latch"):
        robot.push("the gripper into latch")

# button-press-bottomup: press the button up from the bottom
def button_press_bottomup(robot):
    if check("the robot's gripper is not near button"):
        robot.put("gripper below button")
    if check("the robot's gripper is near button"):
        robot.push("button up")

# peg-insert-topdown: grab the peg and insert it into the hole from the top down
def peg_insert_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not right of the robot's gripper and peg is not forward aligned with the robot's