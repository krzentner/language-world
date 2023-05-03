
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above the wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not above the goal location"):
        robot.reach("over the wall to target")