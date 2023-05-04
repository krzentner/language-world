
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper right.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("around the door handle")

# pick-place-side: grab the puck and place it down from the side
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper to the side of the puck
    #  2. Close the gripper around the puck
    #  3. Lift the puck up
    #  4. Move the puck to the target location
    # To pick up the puck from the side, we can close the gripper around the
    # puck and then lift it up to pick it up.
    if check("the robot's gripper is not forward aligned with the puck"):
        robot.move_gripper("vertical