
    if check("the robot's gripper is not near lever handle"):
        robot.put("the gripper near lever handle")
    if check("the robot's gripper is below lever handle"):
        robot.grab("lever handle")
    if check("the robot's gripper is right of lever handle"):
        robot.move("gripper to lever handle")
    if check("the robot's gripper is in front of lever handle"):
        robot.lift("the lever up")

# button-press-side: push the button forward from the side
def button_press_side(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not below button"):
        robot.put("gripper near button")
    if check("the robot's gripper is below button and the robot's gripper is not near button"):
        robot.move("gripper to button")
    if check("the robot's gripper is near button and the robot's gripper is not left of button"):
        robot.slide("gripper to side of button")
    if check("the robot's gripper is left of button and the robot's gripper is not horizontally aligned with button"):
        robot.move("gripper to button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is closed"):
        robot.move("gripper back from button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is open"):
        robot.push("button in")

# lever-push: rotate the lever down
def lever_push(robot):
    if check("the robot's gripper is not near lever handle"):
        robot.put("gripper above lever handle")
    if check("the robot's gripper is vertically aligned with lever handle and the robot's gripper is open"):
        robot.put("gripper around lever handle")
    if check("the robot's gripper is above lever handle"):
        robot.lift("lever up a little")
    if check("the robot's gripper is right of lever handle"):
        robot.push("lever down")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move("gripper to