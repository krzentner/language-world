if check("the plate is not in front of the robot's gripper"):
        robot.move("gripper in front of the plate")
    if check("the robot's gripper is not above the plate"):
        robot.move("gripper above the plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the plate is below the robot's gripper and the robot's gripper is closed"):
        robot.slide("the plate to the target location")