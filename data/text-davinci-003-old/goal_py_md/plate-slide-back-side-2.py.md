

Steps:
  1. Put gripper above the plate
  2. Drop gripper around the plate
  3. Slide the plate back sideways into the target location

# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is around the plate, slide the plate to the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("horizontally aligned with the target location")