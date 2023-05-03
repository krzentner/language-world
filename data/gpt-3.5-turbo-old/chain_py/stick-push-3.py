# Steps:
    #  1. Position the stick in front of the thermos
    #  2. Push the thermos to the target location using the stick
    # We can position the stick by moving the robot's gripper and arm to place it
    # in front of the thermos at the right angle.
    if check("the stick is not in front of the thermos"):
        robot.position("stick in front of thermos")
    # Once the stick is in the right position, we can push the thermos using the
    # stick by moving it towards the target location.
    if check("the stick is in front of the thermos"):
        robot.push("thermos to the goal using the stick")