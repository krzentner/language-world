if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the goal location"):
        robot.align("plate to goal location")
    if check("the plate is horizontally aligned with the goal location"):
        robot.slide("plate sideways into the goal location")