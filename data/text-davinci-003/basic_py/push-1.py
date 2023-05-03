
    if check("the robot's gripper is not horizontally aligned with puck"):
        robot.place("gripper in front of puck")
    if check("the robot's gripper is not touching puck"):
        robot.grab("puck")
    if check("the robot's gripper is gripping puck"):
        robot.slide("puck to goal")