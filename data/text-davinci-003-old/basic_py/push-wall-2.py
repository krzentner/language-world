
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("gripper into the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is below the wall"):
        robot.slide("the puck past the wall to the goal")