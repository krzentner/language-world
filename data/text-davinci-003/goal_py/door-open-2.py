
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around the door handle
    #  3. Pull open the door
    # We need to line up the gripper in front of the door handle.
    # Because it's a door, we can just line it up from the front, since it's
    # easier to line it up from the front than trying to move it around the door
    # handle.
    if check("the robot's gripper is not forward aligned with the door handle"):
        robot.move_gripper("forward aligned with the door handle")
    # Now that the gripper is lined up, move it around the door handle to grasp
    # it.
    # Unlike a drawer, the gripper should not move in front of the door handle, or
    # it will hit the door when we try to pull the door open.
    if check("the robot's gripper is forward aligned with the door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Now that we have the door handle in the gripper, pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")