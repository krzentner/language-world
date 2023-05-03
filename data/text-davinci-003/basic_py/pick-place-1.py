
    if check("the robot's gripper is not above puck and the robot's gripper is below the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is above the puck and the  robot's gripper is not near puck"):
        robot.grab("the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.place("the puck at goal")