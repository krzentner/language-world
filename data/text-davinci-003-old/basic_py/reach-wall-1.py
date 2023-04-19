
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is not near the wall"):
        robot.put("gripper near wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not vertically aligned with the target location"):
        robot.reach("above wall to target")