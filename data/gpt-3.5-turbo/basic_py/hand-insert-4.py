    if check("the puck is not left and below the robot's gripper"):
        robot.move("gripper to left and above the puck")
    if check("the robot's gripper is above and around the puck and the puck is not at the goal"):
        robot.move("gripper to the goal")
    if check("the robot's gripper is above and around the puck and the puck is at the goal"):
        robot.release("gripper and leave the puck at the goal")