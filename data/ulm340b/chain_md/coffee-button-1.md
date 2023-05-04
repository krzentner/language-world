
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `window-close-topdown` requires the robot to slide the window closed to the right, viewed from above.
To slide the window closed to the right, viewed from above reliably, what steps the robot should perform?
    Steps:  1. Move gripper to left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the robot's gripper is not left of the window handle, we should move the gripper near the window handle to start pushing.
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `drawer-open-side` requires the robot to pull the drawer open, seen from the side.
To pull the drawer open, seen from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper vertically above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    First, put the gripper above the drawer handle. Because the angle of the robot's gripper means that we can only grab the drawer handle from the side, we should put the gripper above the drawer handle from the side.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When