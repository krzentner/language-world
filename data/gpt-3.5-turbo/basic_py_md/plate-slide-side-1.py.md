# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the plate is not left of the robot's gripper and the robot's gripper is not around plate"):
        robot.grab("plate")
    if check("the robot's gripper is around plate"):
        if check("the plate is not right of the target location and the robot's gripper is above the target location"):
            robot.move("gripper to right of target location")
        if check("the robot's gripper is beside the target location"):
            robot.push("plate into target location")