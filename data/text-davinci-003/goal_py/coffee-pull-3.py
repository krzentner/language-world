
    # Steps:
    #  1. Put gripper above the mug
    #  2. Close the gripper on the mug
    #  3. Move the mug to the target location
    # First, move the gripper above the mug.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't near the mug, move the gripper near the mug to trap it
    # with the gripper.
    if check("the robot's gripper is not near mug"):
        robot.move_gripper("near the mug", close_gripper=True)
    # Once the gripper is around the mug, start pulling the mug to the target
    # location.
    if check("the robot's gripper is near the mug"):
        robot.move_gripper("around the target location")