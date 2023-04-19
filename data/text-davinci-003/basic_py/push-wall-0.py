
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.lift("the puck over the wall")
    if check("the wall is blocking the path of the puck"):
        robot.push("the puck around the wall")
    if check("there is enough space to move the puck around the wall"):
        robot.slide("the puck to the goal")