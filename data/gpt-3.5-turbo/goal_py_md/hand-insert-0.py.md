# hand-insert: pick up the object and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper roughly above the object
    #  2. Drop gripper around the object
    #  3. Close gripper around the object
    #  4. Move the object to the target location
    # First, put the gripper roughly above the object so that we minimize the
    # chances of bumping into it while closing the gripper.
    if check("the robot's gripper is not above the object"):
        robot.move_gripper("above the object")
    # If the gripper isn't around the object, put it around the object.
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.move_gripper("near the object", close_gripper=True)
    # If the gripper is around the object, we can move the object to the target
    # location.
    if check("the robot's gripper is around object"):
        robot.move_gripper("above the target location")