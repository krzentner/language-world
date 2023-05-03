# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not above button and the robot's gripper is not vertically aligned with the button"):
        robot.put("the gripper above the button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near button"):
        robot.push("the gripper into the button")
    if check("the robot's gripper is near the button and the button is below the robot's gripper"):
        robot.push("the button down")