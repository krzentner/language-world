

# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the the door handle is left of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the door handle is left of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move("gripper to right of door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is near the door handle"):
        robot.slide("door right")
    # If the robot's gripper is starting to be in front of the door handle,
    # push harder.
    if check("the robot's gripper is in front of the door handle"):
        robot.push("door right harder")