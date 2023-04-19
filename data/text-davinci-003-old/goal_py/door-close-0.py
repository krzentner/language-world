
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    # If the robot's gripper is not near the door handle, we should move it near
    # the door handle to start pushing.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # Once the gripper is near the door handle, push the door closed.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")
    # If the robot's gripper is starting to be in front of the door handle, push
    # harder.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("left of the door handle")