
    if check("the robot's gripper is above button"):
        robot.slide("into button")
    if check("the robot's gripper is near button"):
        robot.push("button into the wall")
    if check("the robot's gripper is near button and the robot's gripper is at the top of the button"):
        robot.slide("along top of button")
    if check("the robot's gripper is left of button"):
        robot.place("gripper above button")
    if check("the robot's gripper is above button"):
        robot.push("into button")
    if check("the robot's gripper is near button"):
        robot.push("button into the wall")

# button-press-topdown-wall: push the button down from above with a tall wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is vertically aligned with button"):
        robot.put("gripper near button")
    if check("the robot's gripper is near button"):
        robot.push("into button")
    if check("the robot's gripper is near button and the robot's gripper is above the button"):
        robot.slide("along top of button")
    if check("the robot's gripper is left of button"):
        robot.put("gripper vertically aligned with button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.slide("down into button")

# button-press-side: push the button from the side with a short wall in the way
def button_press_side(robot):
    if check("the robot's gripper is left of button"):
        robot.grab("button")
    if check("the robot's gripper is near button"):
        robot.push("button into wall")
    if check("the robot's gripper is near button and the robot's gripper is above button"):
        robot.slide("above button")
    if check("the robot's gripper is left of button and the robot's gripper is forward aligned with button"):
        robot.push("gripper into button")
    if check("the robot's gripper is near button"):
        robot.push("button into wall")

# button-press-side-wall: push the button from the side with a tall wall in the