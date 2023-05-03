if check("the robot's gripper is not near the puck"):
        robot.move("gripper to above the puck")
    if check("the robot's gripper is above the puck and the gripper is not closed"):
        robot.grab("the puck")
    if check("the puck is in the gripper and the gripper is not near the goal"):
        robot.move("gripper to above the goal")
    if check("the puck is in the gripper and the gripper is above the goal"):
        robot.release("the puck")