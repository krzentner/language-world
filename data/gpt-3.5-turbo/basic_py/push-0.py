if check("the puck is not between the robot's gripper and the goal"):
        robot.move("gripper above the puck")
    if check("the robot's gripper is around the puck"):
        robot.push("puck towards goal")
    if check("the puck is at the target location"):
        robot.stop("pushing")