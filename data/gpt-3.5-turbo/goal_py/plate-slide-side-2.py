# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Align the gripper and plate with the opening
    #  4. Slide the plate towards the opening
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is lined up above the plate, grab it by moving the
    # gripper down around it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the plate is grabbed, align the gripper and plate with the opening by
    # moving the gripper to the side of the opening.
    if check("the robot's gripper is around the plate and the robot's gripper is not near the opening"):
        robot.move_gripper("left of the opening")
    # Finally, slide the plate towards the opening by moving the gripper closer
    # to the opening.
    if check("the robot's gripper is near the opening"):
        robot.move_gripper("horizontally aligned with the opening")