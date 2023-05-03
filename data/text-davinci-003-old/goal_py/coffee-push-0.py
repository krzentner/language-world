
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to target
    # We need to put the gripper above the mug to be able to move it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # We don't need to be careful with the direction, because there is only one
    # way to fit the mug into the gripper.
    if check("the robot's gripper is not around the mug"):
        robot.move_gripper("near the mug", close_gripper=True)
    # Once the mug is in the gripper, just move it to the target location.
    if check("the robot's gripper is around the mug"):
        robot.move_gripper("above the target location")