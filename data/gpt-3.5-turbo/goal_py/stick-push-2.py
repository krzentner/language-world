# Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line the stick up with the thermos
    #  4. Push the thermos to the target location with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper isn't around the stick, we need to move it into position to
    # grab the stick.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the gripper is around the stick, we can use it to push the thermos.
    # Line the stick up with the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("above the thermos")
    # If the stick is lined up with the thermos, we can push the thermos with it.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("almost vertically aligned with the thermos")