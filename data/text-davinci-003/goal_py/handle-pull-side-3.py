
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up on the the handle
    # We need to position the gripper above the handle to grab it.
    if check("the robot's grip is not above the handle"):
        robot.move_gripper("above the handle")
    # Since the handle is something you can only grip with your fingers (as
    # opposed to insert a peg or activate a door or window), we should close the
    # gripper on the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Once the gripper is around the handle and has a good grip, we can begin to
    # pull up the handle by moving the gripper up.
    if check("the robot's gripper is around the handle and the robot's gripper is not near the target location"):
            robot.move_gripper("near the target location")