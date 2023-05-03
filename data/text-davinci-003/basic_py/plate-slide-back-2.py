
    if check("the robot's gripper is open and the robot's gripper is not near the plate"):
        robot.grab("the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.close("the gripper around the plate")
    if check("the robot's gripper is forward aligned with the plate and the robot's gripper is closed"):
        robot.slide("the plate back to the goal")