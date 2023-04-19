# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Position the gripper to hold the stick
    #  2. Move the stick into position slightly behind the thermos
    #  3. Move the gripper down to hold the stick in place
    #  4. Move the gripper forward to push the thermos
    #  5. Release the gripper to let go of the stick
    # First, position the gripper to hold the stick.
    if check("the robot's gripper is not positioned above the stick and the gripper is open"):
        robot.move_gripper("above the stick")
    # Once the gripper is positioned above the stick, move the stick
    # into position slightly behind the thermos.
    if check("the robot's gripper is above the stick and the stick is not positioned behind the thermos"):
        robot.move_gripper("behind the thermos")
    # Once the stick is behind the thermos, move the gripper down to hold
    # the stick in place.
    if check("the robot's gripper is positioned behind the thermos and the gripper is open"):
        robot.move_gripper("holding the stick")
    # Now that the stick is being held in place, move the gripper forward
    # to push the thermos.
    if check("the robot's gripper is holding the stick and the stick is not pushing the thermos"):
        robot.move_gripper("pushing the thermos")
    # After the thermos has been pushed, release the gripper to let go of the stick.
    if check("the robot's gripper is pushing the thermos"):
        robot.move_gripper("above the stick", open_gripper=True)