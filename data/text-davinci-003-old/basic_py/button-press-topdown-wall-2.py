
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not in front of the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is in front of the button and the robot's gripper is not above the button"):
        robot.reach("around wall")
    if check("the robot's gripper is above the button and the robot's gripper is not vertically aligned with the button"):
        robot.align("gripper with button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")