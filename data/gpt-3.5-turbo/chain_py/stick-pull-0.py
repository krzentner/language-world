# Steps:
    #  1. Put gripper around stick and grab it
    #  2. Line up stick with the thermos handle
    #  3. Pull the stick towards the target location to move the thermos
    # First, put the gripper around the stick and grab it.
    if check("the robot's gripper is not around stick"):
        robot.grab("stick")
    # Once the gripper is around the stick, line up the stick with the thermos
    # handle.
    if check("the robot's gripper is around stick and the stick is not aligned with thermos handle"):
        robot.align("stick with thermos handle")
    # Once the stick is lined up with the thermos handle, we can pull the stick
    # towards the target location to move the thermos.
    if check("the stick is aligned with thermos handle"):
        robot.pull("stick towards target location")