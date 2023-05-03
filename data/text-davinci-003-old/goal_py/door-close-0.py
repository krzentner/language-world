
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # First, put the gripper left of the door handle.
    if check("the robot's gripper is not left of the door handle"):
        robot.move_gripper("left of the door handle")
    # If the gripper is near the door handle and the door isn't lined up with the
    # gripper, line the door up with the gripper
    if check("the robot's gripper is near and left of the door handle and the door handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the door handle")
    # If the door is lined up with the gripper, push the door closed.
    if check("the robot's gripper is forward aligned  with the door handle"):
        robot.move_gripper("right of the door handle")