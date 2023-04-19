
    if check("the robot's gripper is not above the wall"):
        robot.reach("above wall")
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above the button and the robot's gripper is open"):
        robot.drop("gripper on button")
    if check("the robot's gripper is on the button"):
        robot.push("down on button")