# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the gripper to the target location
    #  4. Slide the plate sideways to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a flat object, we need to check if the gripper is
    # around it and not just above it.
    if check("plate is not left of the gripper and the plate is not grasped by the gripper"):
        robot.grab("plate")
    # Once the gripper has the plate, move it to the target location.
    if check("the plate is grasped by the gripper and the gripper is not at the target location"):
        robot.move("gripper to target location")
    # If the plate is at the target location and not already slid to the side,
    # slide it sideways.
    if check("the plate is at the target location but not horizontally aligned with the target location"):
        robot.slide("plate sideways to target location")