# Steps:
    # 1. Put gripper above plate
    # 2. Grab the plate with the gripper
    # 3. Slide the plate towards the target location
    # First, put the gripper above the plate
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is above the plate but not around it, put it around the plate
    if check("the robot's gripper is not around the plate" and "the robot's gripper is above the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # If the gripper is around the plate, slide it towards the target location
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the target location")