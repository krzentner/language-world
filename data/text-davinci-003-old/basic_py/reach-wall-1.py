
    if check("the robot's gripper is not above reach target"):
        robot.reach("to goal")
    if check("the robot's gripper is not above wall and the wall is in the path towards the target"):
        robot.reach("around wall")