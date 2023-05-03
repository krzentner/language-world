if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.move("gripper to the side of the plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the plate is not at the target location"):
        robot.slide("plate sideways to the target location")