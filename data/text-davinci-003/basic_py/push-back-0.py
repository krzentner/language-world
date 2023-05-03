
    if check("the robot's gripper is not behind puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper behind the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")