# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the gripper to the target area
    #  4. Slide the plate back sideways into the target location
    # Put the gripper roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.drop("gripper around the plate")
    # If the gripper is around the plate, move it to the target area.
    if check("the robot's gripper is around the plate and the robot's gripper is near the target area"):
        robot.move("gripper to target area")
    # If the gripper is near the target area, slide the plate back into the target location.
    if check("the robot's gripper is near the target area"):
        robot.slide("plate back sideways into the target location")