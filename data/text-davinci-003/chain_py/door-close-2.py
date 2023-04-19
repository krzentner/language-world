
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the door handle is right of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move("gripper to left of door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door close now by moving the gripper right.
    if check("the robot's gripper is near the door handle"):
        robot.slide("door right")
    # If the robot's gripper is starting to be in front of the door handle,
    # push harder.
    if check("the robot's gripper is in front of the door handle"):
        robot.push("door right harder")