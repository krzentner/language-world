# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the gripper to the target location
    #  4. Slide the plate back into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a flat object, check if the gripper is lined up with it
    # from any side instead of around it.
    if check("plate is not left of the robot's gripper and plate is not vertically aligned with the robot's gripper"):
        robot.move_gripper("near the plate", close_gripper=True)
    # We have the plate now, so move it to the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, slide the plate to the back and
    # put it down.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("horizontally aligned with the target location")