
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not aligned with button"):
        robot.align("gripper with button")
    if check("the robot's gripper is aligned with button and the robot's gripper is open"):
        robot.close("gripper")
    if check("the robot's gripper is not above button and the robot's gripper is closed