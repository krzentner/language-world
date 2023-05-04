
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.put("gripper above window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# window-lock: turn the window lock to the closed position
def window_lock(robot):
    # Steps:
    #  1. Put gripper above window lock
    #  2. Turn window lock left
    # To turn the window lock, the robot can hold the lock and turn the gripper
    # from the side.
    # The robot needs to have the gripper below the window lock.
    if check("the robot's gripper is not vertically aligned with the window lock"):
        robot.put("gripper above window lock")
    # Now that the gripper is above the lock, we should try to grab the lock and
    # turn it.
    if check("the robot's gripper is vertically aligned with the window lock"):
        robot.turn("window lock left")

# window-unlock: turn the window lock to the open position
def window_unlock(robot):
    # Steps:
    #  1. Put gripper above window lock
    #  2. Turn window lock right
    # To turn the window lock, the robot can hold the lock and turn the gripper
    # from the side.
    # The robot needs to have the gripper below the window lock.
    if check("the robot's gripper is not