if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button and there is a wall in front of the gripper"):
        robot.move("gripper right")
    if check("the robot's gripper is vertically aligned with button and there is no wall in front of the gripper"):
        robot.push("down on button")