# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Position the gripper above the target location
    #  4. Slide the plate to the target location by moving the gripper
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not grabbed by the gripper, grab it with the gripper
    if check("the robot's gripper is not around the plate" and "the robot's gripper is open"):
        robot.move_gripper("above the plate", close_gripper=True)
    # Position the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Move the gripper down while sliding the plate to the target location
    while check("the robot's gripper is above the target location" and "the plate is below the robot's gripper"):
        robot.move_gripper("near the target location")