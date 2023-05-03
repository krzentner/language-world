# plate-slide: slide the plate into the target location
def plate_slide(robot):
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is above the plate and the robot's gripper is closed and the plate is not aligned with the target location"):
        robot.align("plate to target location")
    if check("the plate is aligned with the target location"):
        robot.slide("the plate to the goal")