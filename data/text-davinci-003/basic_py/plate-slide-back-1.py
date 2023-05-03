
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.put("gripper forward aligned with plate")
    if check("the robot's gripper is near the plate and the plate is not at the goal"):
        robot.slide("the plate to the goal")