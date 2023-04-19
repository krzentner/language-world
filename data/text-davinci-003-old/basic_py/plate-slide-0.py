
    if check("the robot's gripper is not near the plate"):
        robot.move("gripper above the plate")
    if check("the robot's gripper is near the plate and the plate is not in the target location"):
        robot.grab("plate")
    if check("the robot's gripper is near the plate and the plate is in the target location"):
        robot.slide("the plate to the goal")