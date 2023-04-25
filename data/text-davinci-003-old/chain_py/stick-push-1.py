
    # Steps:
    #  1. Move the gripper to the end of the stick
    #  2. Put the stick in front of the thermos
    #  3. Push the thermos with the stick
    # First, move the gripper to the end of the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move("gripper to end of stick")
    # If the stick isn't in front of the thermos, put it in front of the thermos.
    if check("the stick is not in front of the thermos"):
        robot.put("stick in front of thermos")
    # Once the stick is in front of the thermos and the gripper is near the
    # stick, push the thermos with the stick.
    if check("the stick is in front of the thermos and the robot's gripper is near the stick"):
        robot.push("thermos with stick")