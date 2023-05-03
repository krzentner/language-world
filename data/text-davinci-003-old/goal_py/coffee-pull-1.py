
    # Steps
    #  1. Put gripper roughly above the mug
    #  2. Drop gripper around the mug
    #  3. Close gripper around mug
    #  4. Move mug to goal
    # First, put the gripper roughly above the mug so that we don't bump it while
    # grabbing it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the mug is not below the gripper, move the gripper around the mug so
    # that it is below it and then close the gripper.
    # We assume the goal is below the starting position.
    if check("the robot's gripper is not around the mug"):
        robot.move_gripper("below the mug", close_gripper=True)
    # Now that the gripper is around the mug, move it to the target location.
    if check("the robot's gripper around the mug and the robot's gripper is not near the goal"):
        robot.move_gripper("near the goal")