if check("the puck is not in front of the robot's gripper"):
        robot.move("gripper to the side of the puck")
    if check("the robot's gripper is near the puck"):
        robot.push("puck towards the goal")
    if check("the puck is at the goal"):
        robot.celebrate("with a happy dance")