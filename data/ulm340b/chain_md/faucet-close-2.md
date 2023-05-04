
    Steps:  1. Put gripper above the faucet handle  2. Grab the faucet handle with the gripper  3. Rotate the faucet  4. Release the faucet handle
    Put the gripper above the faucet handle to start grabbing it.
    - When the robot's gripper is not vertically aligned with the faucet handle, the robot should put gripper above faucet handle.
    If the robot's gripper is around the faucet handle, rotate the handle by moving the gripper left.
    - When the robot's gripper is around faucet handle, the robot should rotate faucet.
    If the gripper is right of the faucet handle, release the faucet handle.
    - When the robot's gripper is right of the faucet handle, the robot should release faucet handle.

The task `pick-place-side` requires the robot to pick up the puck and hold it to the side of the target location.
To pick up the puck and hold it to the side of the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Slide the puck to the goal
    First, put the gripper above the puck.
    - When the robot's gripper is not above the puck, the robot should put gripper above puck.
    Once the gripper is roughly above the puck, we can grab it.
    - When the robot's gripper is above puck, the robot should drop gripper around puck.
    If the gripper is still roughly around the puck and open, maybe we grabbed the puck. Try sliding it to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should slide puck to goal.

The task `window-open-v2` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder
    If the window handle is left of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window handle is left of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to right of window handle.
    If the