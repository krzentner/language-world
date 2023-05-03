
    # Steps:
    #  1. Put gripper above the mug
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Pull mug towards goal
    # The robot needs to line up the gripper vertically with the mug, so that it
    # can put the gripper around the mug handle.
    # If the robot's gripper isn't vertically aligned with the mug, move the
    # gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the mug isn't aligned with the gripper as seen from in front, we can grab
    # it.
    if check("the robot's gripper is forward aligned with the mug and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Now that the gripper is around the mug handle, we can pull the mug towards
    # the goal. We don't need to be careful about the direction, since the mug
    # handle is large.
    if check("the robot's gripper is around the mug handle and the robot's gripper is not near target location"):
        robot.move_gripper("near the target location")