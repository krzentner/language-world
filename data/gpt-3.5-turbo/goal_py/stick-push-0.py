# Steps:
    #  1. Put gripper above stick
    #  2. Grab the stick with the gripper
    #  3. Line the stick up with the thermos
    #  4. Push the thermos to the target location using the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the stick is not yet in the gripper, grab it by moving the gripper down
    # around it.
    if check("the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    # Once the gripper is around the stick, line it up with the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("horizontally aligned with the thermos")
    # Once the stick is lined up with the thermos, use it to push the thermos to
    # the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("alongside the thermos")