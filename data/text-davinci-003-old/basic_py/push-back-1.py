
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above the puck and the robot's gripper is not near puck"):
        robot.push("gripper into puck")
    if check("the robot's gripper is near the puck"):
        robot.slide("puck back")