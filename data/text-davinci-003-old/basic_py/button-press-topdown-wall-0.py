
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is above the wall, but not near the button"):
        robot.move("gripper around wall")
    if check("the robot's gripper is near the button and the gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("down on button")