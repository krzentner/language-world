if check("the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is near the target location"):
        robot.push("puck to goal")
    if check("the robot's gripper is at the target location"):
        robot.release("puck")