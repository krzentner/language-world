# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is around the plate and the plate is not at the starting point"):
        robot.pull("plate back sideways")
    if check("the gripper is above the goal location"):
        robot.push("plate in goal location")