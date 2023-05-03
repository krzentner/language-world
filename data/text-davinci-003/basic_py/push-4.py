
    if check("puck is not near the robot's gripper and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.push("puck towards goal")