# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
if check("the robot's gripper is not above plate"):
    robot.pick("the gripper above the plate")
if check("the robot's gripper is not holding the plate"):
    robot.grab("the plate")
if check("the robot's gripper is holding the plate and the gripper is not near the target location"):
    robot.move("the gripper to the target location")
if check("the gripper is sideways and not touching anything"):
    robot.slide("the plate back into the target location")