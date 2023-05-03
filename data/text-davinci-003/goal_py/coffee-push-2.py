
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around the mug
    #  3. Move the mug by pushing with the gripper
    # First, move the gripper above the mug.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug"):
        robot.move_gripper("around the mug")
    # Move the mug by pushing down on it with the gripper.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("near the target location")