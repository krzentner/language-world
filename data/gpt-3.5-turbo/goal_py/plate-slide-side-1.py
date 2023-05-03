# Steps:
    #  1. Position gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Close gripper around the plate
    #  4. Move the plate to the target location, dragging it against the surface
    # First, position the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate but not around the plate, drop it around
    # the plate and close the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # With the plate gripped, we can slide it to the target location by dragging
    # it along the surface. 
    if check("the robot's gripper is around the plate and the robot's gripper is not near the target location"):
        robot.move_gripper("vertically aligned with target location", close_gripper=True)