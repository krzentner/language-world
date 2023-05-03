
    # Steps:
    #  1. Put the stick against the back of the thermos
    #  2. Push the stick forward, pushing the thermos with it
    # First, put the stick against the back of the thermos.
    if check("the stick is not behind the thermos"):
        robot.push("stick against back of thermos")
    # If the stick is in place, we can try to move the thermos forward.
    if check("the stick is behind the thermos and the robot's gripper is open"):
        robot.push("stick forward, pushing thermos")
    # If the thermos was pushed far enough away, we can move it to the target
    # location by pushing the stick against it again.
    if check("the thermos is far enough away"):
        robot.push("stick again, pushing thermos to goal")