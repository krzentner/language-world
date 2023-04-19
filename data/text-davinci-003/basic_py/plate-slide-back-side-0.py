
    if check("the robot's gripper is below the plate and the robot's gripper is not near the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is near the plate and the plate is not horizontally aligned with the goal"):
        robot.slide("plate to goal")
    if check("the plate is horizontally aligned with the goal"):
        robot.pull("plate back")