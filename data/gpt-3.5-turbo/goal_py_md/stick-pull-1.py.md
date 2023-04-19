# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put gripper above one end of the stick
    #  2. Drop gripper around the stick
    #  3. Close gripper around the stick
    #  4. Move the other end of the stick to the thermos
    #  5. Slide the thermos to the target location by pulling it with the stick
    #  6. Release the stick
    # First, put the gripper roughly above one end of the stick.
    if check("the robot's gripper is not above one end of the stick"):
        robot.move_gripper("above one end of the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick, we can now move the other end of the
    # stick to the thermos.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("above the thermos")
        # We can now slide the thermos to the target location by pulling it with
        # the stick.
        if check("the robot's gripper is above the thermos and the robot's gripper is holding the stick"):
            robot.move_gripper("near the target location")
            # Release the stick to complete the task.
            if check("the robot's gripper is near the target location"):
                robot.move_gripper("above one end of the stick", open_gripper=True)