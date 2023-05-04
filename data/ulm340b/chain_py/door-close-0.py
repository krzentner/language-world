
    # Steps:
    #  1. Put gripper above door handle
    #  2. Grab the door handle by moving the gripper around it
    #  3. Push the door closed
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the door handle and the robot's gripper is not almost vertically aligned with the door handle"):
        robot.put("the gripper above the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around the door handle"):
        robot.put("gripper around the door handle")
    # Once the gripper is around the door handle, we can just push the door
    # closed.
    if check("the robot's gripper is around the door handle"):
        robot.push("the door closed")

# window-close: slide the window closed
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("the gripper to the left of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("the window to the right")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("the window to the right harder")

# reach: reach to