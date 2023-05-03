# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the gripper to the left side of the plate
    #  4. Move the gripper to the back of the plate
    #  5. Slide the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is above the plate, grab the plate with the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the gripper has grabbed the plate, move the gripper to the left side
    # of the plate.
    if check("the robot's gripper is around the plate and the plate is not left of the robot's gripper"):
        robot.move_gripper("left of the plate")
    # Once the gripper is on the left side of the plate, move it to the back of
    # the plate.
    if check("the robot's gripper is left of the plate and the plate is not behind the robot's gripper"):
        robot.move_gripper("behind the plate")
    # Once the gripper is behind the plate, slide the plate sideways into the
    # target location.
    if check("the robot's gripper is behind the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")