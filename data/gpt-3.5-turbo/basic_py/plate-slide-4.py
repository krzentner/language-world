if check("the robot's gripper is not above the plate"):
        robot.move("gripper above plate")
    if check("the plate is not in the robot's gripper and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.grab("plate")
    if check("the robot's gripper is vertically aligned with the target location and the plate is in the robot's gripper"):
        robot.slide("plate into target location")