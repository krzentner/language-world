if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        if check("there is a wall between the puck and the goal"):
            robot.push("the puck towards the wall")
            robot.slide("the puck along the wall")
            robot.push("the puck towards the goal")
        else:
            robot.slide("the puck to the goal")