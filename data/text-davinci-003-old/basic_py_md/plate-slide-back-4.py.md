

If check("the robot's gripper is not near the plate"):
    robot.reach("to plate")
if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is above the plate and the plate is not near target"):
    robot.slide("plate to target")
if check("the plate is near the target"):
    robot.slide("plate into target")