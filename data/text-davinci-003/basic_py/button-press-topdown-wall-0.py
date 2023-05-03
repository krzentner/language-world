
    if check("the robot's gripper is not vertically aligned with button and the wall is between the button and the robot's gripper"):
        robot.put("gripper above button")
    if check("the wall is not between button and the robot's gripper and the robot's gripper is not above button"):
        robot.move("along wall")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")