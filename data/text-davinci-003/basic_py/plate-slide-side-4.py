
    if check("the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.grab("the plate")
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.slide("the plate to the horizontal alignment of the target location")
    if check("the plate is horizontally aligned with the target location"):
        robot.slide("the plate to the target location")