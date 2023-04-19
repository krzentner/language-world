
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("puck towards the wall")
    if check("the robot's gripper is pressing at the wall"):
        robot.slide("puck around the wall")
    if check("puck is past the wall"):
        robot.slide("puck to the goal")