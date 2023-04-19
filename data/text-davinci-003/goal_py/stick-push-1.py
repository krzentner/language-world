
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Put the stick roughly parallel to the thermos 
    #  4. Push the thermos with the stick
    # first, put the gripper above the stick
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the stick isn't lined up with the thermos, grab it and move it
    # roughly parallel to the thermos.
    if check("the stick is not parallel to the thermos"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the stick is lined up with the thermos, push it to the target location
    # with the stick.
    if check("the stick is parallel to the thermos"):
        robot.move_gripper("near the target location")