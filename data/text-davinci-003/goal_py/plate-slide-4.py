
    # Steps:
    #  1. Put gripper below the plate
    #  2. Grasp the plate
    #  3. Slide the plate to the target location
    # First, put the gripper below the plate.
    if check("the robot's gripper is not below the plate"):
        robot.move_gripper("below the plate")
    # If the gripper is close to the plate but not grasped, close the gripper
    # to get a good grip.
    # This should also bring the plate in line with where it needs to go.
    if check("the robot's gripper is below the plate and the robot's gripper is closed"):
        robot.move_gripper("above the plate")
    # Now that the gripper is around the plate, slide the plate to the target location.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("above the target location")