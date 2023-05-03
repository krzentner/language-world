
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and the robot is not close to wall"):
        robot.reach("close to wall")
    if check("the robot's gripper is vertically aligned with button and the robot is close to wall"):
        robot.push("down on button")