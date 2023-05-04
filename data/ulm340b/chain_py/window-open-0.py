
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# box-close: close the box
def box_close(robot):
    # Steps:
    #  1. Put gripper left of lid
    #  2. Push lid right
    #  3. Push harder to close the box
    # As long as the lid isn't to the left of the gripper, move it.
    if check("the lid is not to the left of the robot's gripper"):
        robot.put("the gripper to the left of the lid")
    # As long as the gripper is near the lid, we can push the lid closed.
    if check("the robot's gripper is near the lid"):
        robot.slide("the lid closed")
    # When the gripper is right of the lid, push the lid hard to close the box.
    if check("the robot's gripper is right of the lid"):
        robot.push("the lid closed")

# box-open: open the box
def box_open(robot):
    # Steps:
    #  1. Put gripper right of lid
    #  2. Push lid left
    #  3. Push harder to open the box
    # As long as the lid isn't to the right of the gripper, move it.
