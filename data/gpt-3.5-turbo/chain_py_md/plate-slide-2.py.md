# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into plate
    #  3. Slide the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above the plate")
    # Once the gripper is above the plate, push it down onto the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not pushing into the plate"):
        robot.push("the gripper into the plate")
    # Once the gripper is pushing into the plate, slide it to the target location.
    if check("the robot's gripper is pushing into the plate"):
        robot.slide("the plate to the target location")