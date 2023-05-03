# Steps:
    #  1. Put gripper to the side of the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate to the target location while keeping it level
    # First, put the gripper to the side of the plate
    if check("the robot's gripper is not to the side of the plate"):
        robot.move_gripper("to the side of the plate")
    # If the gripper is not around the plate, grab it
    if check("the robot's gripper is not around the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Move the plate to the target location while keeping it level
    if check("the plate is not at the target location"):
        robot.move_gripper("above the target location")