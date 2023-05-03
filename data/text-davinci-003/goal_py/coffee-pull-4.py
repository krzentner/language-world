
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Pull mug to goal
    # Put the gripper above the mug.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above mug")
    # If the mug isn't below the gripper as seen from above, move the gripper
    # above the mug.
    if check("mug is not left of the robot's gripper and mug is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the mug")
    # Once the gripper is aligned with the mug, grab the mug by moving the
    # gripper around it.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("around the mug")
    # Pull the mug to the target location.
    if check("the robot's gripper is forward aligned with mug"):
        robot.move_gripper("near the target location")