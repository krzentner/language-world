# Steps:
    #  1. Put gripper left of plate
    #  2. Push gripper against left side of plate to get a grip
    #  3. Slide plate back to target location
    # First, position the gripper to the left of the plate
    # If the gripper is not positioned to the left of the plate, move it there.
    if check("the robot's gripper is not left of the plate"):
        robot.move("the gripper to the left of the plate")
    # If the gripper is left of the plate, push against the left side of the plate to get a grip
    # Wait until robot's gripper is in contact with the plate.
    if check("the robot's gripper is not contacting the plate"):
        robot.push("the gripper against the plate")
    # Once the gripper is in contact with the plate, slide the plate back to the target location
    if check("the robot's gripper is contacting the plate"):
        robot.slide("the plate back to the target location")