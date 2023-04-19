if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is above the plate and the plate is not at the target location"):
        robot.slide("plate sideways to the target location")