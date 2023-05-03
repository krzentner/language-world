
    if check("the robot's gripper is significantly above the puck and the puck is below the robot's gripper"):
        robot.put("gripper above puck")
    if check("the robot's gripper is near the puck and the robot's gripper is not behind the puck"):
        robot.put("gripper behind puck")
    if check("the robot's gripper is behind the puck"):
        robot.slide("puck to goal")
        robot.follow("puck to goal")