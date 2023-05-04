
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# turn-handle: grab the handle and rotate it to be vertical
def turn_handle(robot):
    # Steps:
    #  1. Put gripper vertically above the handle
    #  2. Put gripper around the handle
    #  3. Close gripper
    #  4. Turn the handle clockwise
    #  5. Turn the handle harder
    #  6. Once the handle is vertical, let go of the handle
    # First, line up the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is not above the handle"):
        robot.move("gripper above handle")
    # Now the gripper is above the handle, so we should be able to grab it.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move("gripper around handle")
    # Now the robot's gripper is around the handle, so we should be able to close
    # it.
    if check("the robot's gripper is around the handle"):
        robot.close("gripper")
    # Now the robot's gripper is around the handle and closed, so we should be
    # able to turn it.