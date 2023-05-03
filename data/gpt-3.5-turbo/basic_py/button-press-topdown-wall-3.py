if check("the robot's gripper is not above the short wall and the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above short wall")
    if check("the robot's gripper is above the short wall and the robot's gripper is not vertically aligned with button"):
        robot.move("gripper to above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")