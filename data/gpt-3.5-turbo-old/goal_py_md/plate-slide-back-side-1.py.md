# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate back towards the target in a sideways motion
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not in the gripper, get the gripper around the plate.
    if check("the plate is not in the gripper and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper has the plate, slide the plate back to the target in a sideways motion.
    if check("the plate is in the gripper and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location in a sideways motion")