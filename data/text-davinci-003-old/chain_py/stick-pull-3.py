
    # Steps:
    #  1. Place the stick against the thermos 
    #  2. Move the robot's gripper towards the stick
    #  3. Pull the thermos with the stick
    # First, place the stick gently against the thermos.
    if check("the stick is not touching the thermos"):
        robot.place("stick against thermos")
    # Then, move the robot's gripper so that it is close to the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move("gripper to stick")
    # Now, pull the thermos with the stick, making sure to keep the robot's
    # gripper in contact with the stick.
    if check("the robot's gripper is near the stick"):
        robot.pull("thermos with stick")