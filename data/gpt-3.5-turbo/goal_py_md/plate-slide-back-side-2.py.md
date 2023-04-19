# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    # 1. Put gripper above the plate
    # 2. Grab the plate with the gripper
    # 3. Slide the plate back and to the side into the target location
    # First, put the gripper above the plate
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not between the robot's gripper and the target location, slide it back.
    # We assume the plate is already between the robot's gripper and the starting position.
    if check("the robot's gripper is above the plate and the plate is not at the target location"):
        robot.move_gripper("far from the target location")
        robot.move_gripper("horizontally aligned with the target location", close_gripper=True)
        robot.move_gripper("at the target location")