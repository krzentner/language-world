
    if check("the robot's gripper is not near the wall"):
        robot.move("gripper to wall")
    if check("the robot's gripper is near the wall"):
        robot.reach("over wall to goal")