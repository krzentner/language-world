# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    #  1. Move the gripper to be above the plate
    #  2. Grip the plate
    #  3. Move back to the target location
    #  4. Release the plate
    # First, put the gripper above the plate to be able to grip it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is above the plate, grip the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not gripping the plate"):
        robot.move_gripper("around the plate")
    # Now that the plate is gripped, move back to the target location.
    if check("the robot's gripper is gripping the plate and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Once we're at the target location, release the plate.
    if check("the robot's gripper is above the target location and the robot's gripper is gripping the plate"):
        robot.move_gripper("near the target location", close_gripper=False)