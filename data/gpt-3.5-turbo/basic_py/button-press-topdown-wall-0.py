if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")