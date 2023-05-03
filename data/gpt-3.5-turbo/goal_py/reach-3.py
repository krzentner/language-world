# Steps:
    #  1. Put gripper above target location
    #  2. Move gripper down to target location
    # Reaching involves moving the gripper to the target location without
    # necessarily grabbing anything.
    # First, put the gripper above the target location.
    if check("the robot's gripper is not vertically aligned with target location"):
        robot.move_gripper("vertically aligned with the target location")
    # Then, move the gripper down to the target location.
    if check("the robot's gripper is vertically aligned with the target location and the gripper is not at the target location"):
        robot.move_gripper("at the target location")