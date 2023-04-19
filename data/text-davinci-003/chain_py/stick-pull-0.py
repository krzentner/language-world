
    # Steps:
    #  1. Put the forked end of the stick underneath the thermos
    #  2. Push down the stick until it is securely holding the thermos
    #  3. Pull the thermos to the target location
    # First, the robot needs to put the forked end of the stick under the
    # thermos.
    if check("the stick is not underneath the thermos"):
        robot.place("stick underneath thermos")
    # Once the stick is underneath the thermos, the robot should press down
    #  until it is securely holding the thermos.
    if check("the stick is underneath thermos and the thermos is not securely held by the stick"):
        robot.push("down stick")
    # Once the stick is securing the thermos, the robot can pull the thermos
    # to the target location.
    if check("the the thermos is securely held by the stick"):
        robot.pull("thermos to target location")