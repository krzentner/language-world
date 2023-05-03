
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.drop("gripper near plate")
    if check("the robot's gripper is near the plate and the plate is not sideways aligned with the target location"):
        robot.turn("plate sideways")
    if check("the plate is sideways aligned with the target location and the robot's gripper is not holding plate"):
        robot.grab("plate")
    if check("the robot's gripper is holding the plate"):
        robot.slide("plate back into target location")