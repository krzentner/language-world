# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate back to the target location
    # Since there is no specific guidance on where the plate is initially
    # positioned and how it should be moved, we can assume that the robot's
    # gripper is already near the plate and use a simple approach to slide it
    # back.
    # Move the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate, grab it with the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # Move the plate back to the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the target location")