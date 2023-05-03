# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is above plate and the robot's gripper is closed and the plate is not at the target location"):
        robot.slide("the plate back to the target location")