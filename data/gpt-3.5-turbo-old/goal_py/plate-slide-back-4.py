# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate back to the target location
    # First, put the robot's gripper above the plate
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, grab it with the gripper
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is around the plate, move it back to the target location
    if check("the robot's gripper is around the plate and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")