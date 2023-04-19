# button-press: push the button from the front
# def button_press(robot):
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.grab("button")
    if check("the robot's gripper is not at the right distance from the button"):
        robot.move("gripper closer to button")
    if check("the robot's gripper is at the right distance from the button and the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("the button")