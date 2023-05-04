

''',
        'hidden': False,
        'locked': False,
    },
    {
        'code': r"""
def door_open(robot):
    "*** YOUR CODE HERE ***"
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")

def window_close(robot):
    "*** YOUR CODE HERE ***"
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")

def door_close(robot):
    "*** YOUR CODE HERE ***"
    # Steps:
    #  1. Push the door shut
    #  2. Put gripper above door handle
   