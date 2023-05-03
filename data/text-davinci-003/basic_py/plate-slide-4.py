
    if check("the robot's gripper is not above the plate and the robot's gripper is not forward aligned with the plate"):
        robot.put("gripper above the plate")
    if check("the robot's gripper is forward aligned with the plate and the robot's gripper is not around the plate"):
        robot.drop("gripper around the plate")
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.align("plate to target")
    if check("the plate is horizontally aligned with the target location"):
        robot.slide("plate to goal")