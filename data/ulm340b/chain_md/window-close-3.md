
    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the robot's gripper is not vertically lined up with the window handle, we should move the gripper near the window handle to start pushing
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    If the robot's gripper is near the window handle we can probably slide the window closed now by moving the gripper left.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.

The task `push-back` requires the robot to slide the puck straight back.
To slide the puck straight back reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck back
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it straight back. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide puck backward.

The task `reach-back` requires the robot to reach to the target location behind it.
To reach to the target location behind it reliably, the robot should perform the following steps:
    Steps:  1. Reach back
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location