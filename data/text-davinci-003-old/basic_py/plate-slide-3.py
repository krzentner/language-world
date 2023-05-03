
    if check("the robot's gripper is not near the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not vertically above the plate"):
        robot.hold("the plate")
    if check("the robot's gripper is above the plate"):
        robot.slide("the plate to the goal")