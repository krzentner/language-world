
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to left of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# drawer-close-topdown: push the drawer closed from above
def drawer_close_topdown(robot):
    # Steps:
    #  1. Move the gripper above the drawer handle
    #  2. Put the gripper around the drawer handle
    #  3. Push the drawer closed
    # Move the gripper roughly above the drawer handle so we can push the
    # drawer closed from the side.
    if check("the robot's gripper is not vertically aligned with the drawer handle"):
        robot.put("gripper above drawer handle")
    # Put the gripper around the drawer handle.
    # If the drawer handle is left of the gripper, return to putting the
    # gripper above the drawer handle, since we don't want to grab the drawer
    # handle from the side.
    if check("the robot's gripper is vertically aligned with the drawer handle and the drawer handle is not left of the robot's gripper"):
        robot.put("gripper around drawer handle")
    # Push the drawer closed.
    # If the gripper is still aligned with the drawer handle as seen from in
    # front, the drawer probably isn't closed, so keep pushing.
    if check("the robot's gripper is around drawer