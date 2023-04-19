if check("the robot's gripper is not near the plate and the robot's gripper is not horizontally aligned with the plate"):
        robot.move("gripper to left of plate")
    if check("the robot's gripper is aligned with the plate and the robot's gripper is not around the plate"):
        robot.grab("the plate")
    if check("the robot's gripper is around the plate and the plate is not near the target location"):
        robot.slide("plate to the target location")
    if check("the plate is near the target location and the robot's gripper is aligned with the target location"):
        robot.release("plate at the target location")