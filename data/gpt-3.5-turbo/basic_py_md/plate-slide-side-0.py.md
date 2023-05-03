# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the plate is not left of the robot's gripper and the robot's gripper is not around the plate"):
        robot.grab("plate")
    if check("the robot's gripper is not almost horizontally aligned with the target location"):
        robot.move("gripper near the target location")
    if check("the robot's gripper is almost horizontally aligned with the target location"):
        robot.side_slide("plate into the target location")