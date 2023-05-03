
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Pull open the door
    # First, we need to put the gripper left of the door handle to get it in
    # position.
    if check("the robot's gripper is not left of door handle"):
        robot.move_gripper("left of the door handle")
    # If the robot's gripper is near the door handle, we can pull the door open.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("around the door handle")