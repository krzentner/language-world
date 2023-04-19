
    if check("the robot's gripper is not above the puck and the robot's gripper is below the wall"):
        robot.put("gripper above the wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not near the puck"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")