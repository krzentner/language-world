# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Move stick to thermos
    #  5. Position stick as close to the thermos as possible
    #  6. Push the thermos to the target location using the stick
    # First, put the gripper roughly above the stick, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is near the stick and closed, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above stick and the robot's gripper is closed"):
        robot.move_gripper("near the thermos")
    # If the gripper is near the thermos, we can position the stick as close
    # to the thermos as possible.
    if check("the robot's gripper is near the thermos"):
        robot.move_gripper("at the bottom of the thermos", close_gripper=False)
    # If the stick is as close to the thermos as possible, we can push it to
    # the target location.
    if check("the stick is as close to the thermos as possible"):
        robot.move_gripper("above the target location")