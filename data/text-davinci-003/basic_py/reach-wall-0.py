
    if check("the robot's gripper is not above wall"):
        robot.put("the gripper above the wall")
    if check("the robot's gripper is not near wall and the robot's gripper is open"):
        robot.pull("the gripper into the wall")
    if check("the robot's gripper is near wall and the robot's gripper is open"):
        robot.reach("over wall to goal")