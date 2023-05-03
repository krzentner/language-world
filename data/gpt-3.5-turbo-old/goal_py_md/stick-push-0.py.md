# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Position the stick above the thermos
    #  4. Tilt the stick and push the thermos towards the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the gripper is above the stick, grab it.
    if check("the robot's gripper is above the stick and the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    # If the gripper is around the stick and not above the thermos, put it there.
    if check("the robot's gripper is around the stick and is not above the thermos"):
        robot.move_gripper("above the thermos")
    # If the gripper is above the thermos but the stick isn't tilted towards it,
    # tilt the stick.
    if check("the robot's gripper is above the thermos and the stick is not tilted"):
        robot.tilt_stick("tilted")
    # Once the stick is tilted, push the thermos towards the target location.
    # We might need to move the stick left or right to get it to hit the side of
    # the thermos that faces the target location.
    # TODO: write function to detect which side of the thermos is facing the
    # target location
    if check("the robot's gripper is above the thermos and the stick is tilted"):
        robot.move_stick("to hit the correct side of the thermos", close_gripper=False)