
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not behind puck"):
        robot.push("the gripper behind the puck")
    if check("the robot's gripper is behind the puck and the puck is below the robot's gripper"):
        robot.slide("the puck back to the goal")