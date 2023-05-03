
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle"):
        robot.pull("drawer open")

# button-press-sideways: press the button sideways
def button_press_sideways(robot):
    if check("the robot's gripper is not side aligned with button"):
        robot.align("gripper to side of button")
    if check("the robot's gripper is side aligned with button"):
        robot.push("sideways on button")