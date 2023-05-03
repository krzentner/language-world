# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is near plate and the robot's gripper is open and the plate is below the gripper"):
        robot.close("gripper around plate")
    if check("the robot's gripper is almost vertically aligned with the plate and the robot's gripper is around the plate"):
        robot.pull("plate towards robot")
    if check("the robot's gripper is not forward aligned with the target location and the robot's gripper is around the plate"):
        robot.move("gripper to the left of target location")
    if check("the robot's gripper is forward aligned with the target location and the robot's gripper is around the plate"):
        robot.slide("plate back")