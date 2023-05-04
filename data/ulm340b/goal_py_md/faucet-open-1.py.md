

and write instructions that move the robot's gripper until the faucet handle has turned all the way.

The robot's goal is to make the faucet handle face to the left.

The robot has a single gripper to grab objects, and the gripper can only move up and down.

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    # Steps:
    #  1. Put gripper above the faucet
    #  2. Drop gripper around the faucet
    #  3. Close gripper around the faucet
    #  4. Turn the faucet left
    # First, put the gripper roughly above the faucet, so that we don't bump the
    # faucet handle while trying to grab it.
    if check("the robot's gripper is not above faucet handle"):
        robot.move_gripper("above faucet handle")
    # If the gripper isn't around the faucet handle, put it around the faucet
    # handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.move_gripper("near faucet handle", close_gripper=True)
    # If the gripper is around the faucet handle, the faucet handle should be
    # facing left.
    if check("the robot's gripper is above faucet handle and the robot's gripper is closed and the faucet handle is left"):
        robot.move_gripper("left of the faucet handle")
```
"""

# window-close: slide the window closed to the right
def window_close(robot):
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
        robot