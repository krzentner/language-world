

and then include the rest of your program below that line.
We recommend including comments to describe what your program is doing and why, as we've done in the examples.
"""

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper right of the faucet handle
    #  2. Start pushing against the faucet handle to close the faucet
    #  3. Push the faucet close harder
    # If the faucet handle is left of the robot's gripper, we should move the
    # gripper near the faucet handle to start pushing
    if check("the faucet handle is left of the robot's gripper"):
        robot.move("gripper to right of faucet handle")
    # If the robot's gripper is near the faucet handle we can probably slide the
    # faucet closed now by moving the gripper left.
    if check("the robot's gripper is near the faucet handle"):
        robot.slide("faucet closed")
    # If the robot's gripper is starting to be in front of the faucet handle,
    # push harder.
    if check("the robot's gripper is in front of the faucet handle"):
        robot.push("faucet left harder")

# window-close: slide the window closed to the right
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
    if check("the robot's gripper is in front of the window