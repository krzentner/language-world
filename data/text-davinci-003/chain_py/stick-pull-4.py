
    # Steps:
    #  1. Put gripper near stick handle
    #  2. Put stick handle near thermos
    #  3. Pull the thermos using the stick
    #  4. Pull the thermos using the stick harder
    # First, put the gripper near the stick handle by moving it in the same
    # direction that the stick handle moves when pulled.
    if check("the robot's gripper is not near the stick handle"):
        robot.move("gripper to stick handle")
    # Once we have the stick handle and we start pulling, the handle will arc
    # away from the robot, so we need to put the handle near the thermos.
    if check("the stick handle is not near thermos"):
        robot.put("stick handle near thermos")
    # Now that the thermos is near the stick handle, we can just pull on it.
    if check("the stick handle is near thermos"):
        robot.pull("thermos with stick")
    # If we need more force to move the thermos, pull harder on it.
    if check("the thermos is still not at target location"):
        robot.pull("thermos with stick harder")