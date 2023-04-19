# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    if check("the robot's gripper is not near the plate and the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.drop("gripper around the plate")
    if check("the robot's gripper is around the plate and the plate is not pushed all the way to the back"):
        robot.push("the plate to the back of the target location")
    if check("the plate is pushed to the back"):
        robot.slide("the plate to the target location sideways")