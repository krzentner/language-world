
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with the drawer handle"):
        robot.pull("drawer open")

# grab: grab the object
def grab(robot):
    if check("the robot's gripper is above the object and the gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is near the object and the gripper is open"):
        robot.close("gripper around object")

# button-press-side: press the button to the side
def button_press_side(robot):
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.align("gripper to button")
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.push("button")