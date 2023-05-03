
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate and the plate is not in line with the goal"):
        robot.slide("plate to goal")