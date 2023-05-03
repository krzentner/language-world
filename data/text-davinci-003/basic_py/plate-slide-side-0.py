
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.align("gripper with plate")
    if check("the robot's gripper is horizontally aligned with the plate and the robot's gripper is not near the plate"):
        robot.grab("plate")
    if check("the robot's gripper is near the plate"):
        robot.slide("plate sideways to the goal")