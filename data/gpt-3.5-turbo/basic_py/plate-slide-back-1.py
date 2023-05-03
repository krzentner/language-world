if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.slide("plate back into target location")