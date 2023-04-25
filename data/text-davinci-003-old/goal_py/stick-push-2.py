
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Put the bottom of the stick against the thermos
    #  4. Push the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("above the stick")
    # If the stick is not left of the gripper, go back to putting the gripper
    # above the stick.
    # Because the stick is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # Now that the gripper is lined up with the stick, put the bottom of the
    # stick against the thermos.
    if check("the stick is forward aligned with the thermos"):
        robot.move_gripper("above the stick")
    # Once the bottom of the stick is touching the thermos, slide the thermos
    # to the target location.
    if check("the stick is left of the thermos"):
        robot.move_gripper("near the target location")