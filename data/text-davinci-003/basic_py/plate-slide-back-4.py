
    if check("the robot's gripper is not above the plate and the robot's gripper is not forward aligned with the plate"):
        robot.move("gripper in front of plate")
    if check("the robot's gripper is not horizontally aligned with the target location"):
        robot.align("the plate to the goal")
    if check("the robot's gripper is horizontally aligned with the target location"):
        robot.slide("back the plate to the goal")