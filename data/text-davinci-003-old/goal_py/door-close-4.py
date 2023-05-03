
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Push the door closed
    # If the door handle is right of the robot's gripper, we should move the
    # gripper near the door handle to start pushing.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("right of the door handle")
    # If the robot's gripper is near the door handle we can push the door
    # closed by moving the gripper left.
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move_gripper("left of the target location")