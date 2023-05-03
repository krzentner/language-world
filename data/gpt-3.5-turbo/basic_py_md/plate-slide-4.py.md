# plate-slide: slide the plate into the target location
def plate_slide(robot):
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around plate"):
        robot.grab("plate")
    if check("the robot's gripper is around plate and the robot's gripper is not almost vertically aligned with target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is almost vertically aligned with target location and the target location is not blocked"):
        robot.slide("plate to target location")
    if check("the plate is at the target location"):
        robot.drop("plate")