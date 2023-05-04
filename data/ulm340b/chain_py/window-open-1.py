
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling on the window handle to open the window
    #  3. Pull the window open harder
    # If the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pulling
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is near the window handle"):
        robot.pull("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # pull harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.pull("window left harder")

# window-close: push the button left to right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# peg-insert-topdown: pick up the peg and insert it into the hole from above
def peg_insert_topdown(robot):
  