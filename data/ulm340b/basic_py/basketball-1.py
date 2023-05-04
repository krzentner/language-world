
    if check("the robot's gripper is not vertically aligned with ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is near the ball and the robot's gripper is not above ball"):
        robot.move("gripper above ball")
    if check("the robot's gripper is around ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is around ball and the robot's gripper is closed"):
        robot.move("ball above hoop")
    if check("the robot's gripper is above hoop"):
        robot.move("ball into hoop")

# button-press-side: push the button from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not forward aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above button and the robot's gripper is not forward aligned with the button"):
        robot.move("gripper to button")
    if check("the robot's gripper is near the button"):
        robot.push("the button")

# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not near drawer handle and the robot's gripper is not forward aligned with drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move("drawer handle forward")
    if check("the robot's gripper is in front of drawer handle"):
        robot.push("drawer closed")

# peg-insert-sideway: grab the peg and insert it into the hole from the side
def peg_insert_sideway(robot):
    if check("the robot's gripper is not forward aligned with peg"):
        robot.move("gripper to peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check