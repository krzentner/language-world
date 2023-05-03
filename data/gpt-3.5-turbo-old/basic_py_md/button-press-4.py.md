# button-press: push the button from the front
# def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not aligned with the button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is aligned with the button"):
        robot.move("gripper below the button")
    if check("the robot's gripper is below the button and the robot's gripper is open"):
        robot.grab("button")
    if check("the robot's gripper is around the button and the robot's gripper is not aligned with the button"):
        robot.align("gripper to button")
    if check("the robot's gripper is aligned with the button"):
        robot.push("the button down")