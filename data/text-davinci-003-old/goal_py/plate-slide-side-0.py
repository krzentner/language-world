
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate by dropping gripper around it from above
    #  3. Slide plate sideways
    # To start, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the plate isn't within the robot's gripper, put the gripper around the
    # plate from the top.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the gripper is around the plate, slide it sideways to the target
    # location.
    if check("the robot's gripper is around plate"):
        robot.move_gripper("horizontally aligned with the target location")