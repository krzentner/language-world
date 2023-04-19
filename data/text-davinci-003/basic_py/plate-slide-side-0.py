
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.align("gripper to plate")
    if check("the robot's gripper is horizontally aligned with the plate and the robot's gripper is not near the plate"):
        robot.slide("gripper near to plate")
    if check("the robot's gripper is near the plate and the plate's edge is not at the goal"):
        robot.slide("plate to goal")