
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not near the plate and the robot's gripper is open"):
        robot.drop("gripper near plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.slide("plate back")
    if check("the robot's gripper is near the plate and the robot's gripper is closed"):
        robot.place("plate at goal")