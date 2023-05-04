
    Steps:  1. Put gripper above handle  2. Push gripper into handle
    The robot should put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, the robot should put the gripper above handle.
    If the gripper is lined up above the handle, push it down into the handle.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle, the robot should push the gripper into the handle.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
    Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?
    