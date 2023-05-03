if check("the plate is not in front of the robot's gripper"):
        robot.move("gripper to front of plate")
    if check("the robot's gripper is not above the center of the plate and the robot's gripper is open"):
        robot.drop("gripper above center of plate")
    if check("the robot's gripper is above the center of the plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is around the plate and the plate is not at the target location"):
        robot.slide("plate to target location")
    if check("the plate is at the target location"):
        robot.lift("gripper with plate above target location")