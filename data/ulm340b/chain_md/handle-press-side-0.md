
    Steps:  1. Put gripper roughly around the handle  2. Push down the handle
    If the gripper is not near the handle, move it to the handle. We don't need to be careful about the direction, since the handle is large and we're just pushing it (unlike when opening the handle).
    - When the robot's gripper is not near handle, the robot should grab handle.
    If the handle is aligned with the gripper as seen from in front, we can push the handle down.
    - When the robot's gripper is forward aligned with handle, the robot should push handle down.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    Steps:  1. Put gripper roughly around the button  2. Push down on the button
    If the gripper is not near the button, move it to the button. We don't need to be careful about the direction, since the button is large and we're just pushing it (unlike when opening the button).
    - When the robot's gripper is not near button, the robot should grab button.
    If the button is aligned with the gripper as seen from in front, we can push the button down.
    - When the robot's gripper is forward aligned with button, the robot should push button down.

The task `window-toggle` requires the robot to toggle the window between closed and open.
To toggle the window between closed and open reliably, the robot should perform the following steps:
    Steps:  1. If the window is open, close the window  2. If the window is closed, open the window
    If the window is already closed, open the window. If the window is already closed, open it.
    - When the window handle is not vertically aligned with the robot's gripper, the robot should move gripper right of window handle.
    Once the gripper is aligned with the window handle, start moving the gripper left to open the window.
    - When the window handle is vertically aligned with the robot's gripper, the robot should slide window left.
    If the window is already open, close it.
    - When the window handle is not vertically aligned with the robot's gripper, the robot should move gripper left of window handle.
    Once the gripper is aligned with the window handle, start moving the gripper right to open the window.
    - When the window handle is vertically aligned with the robot's gripper, the robot should slide window right.
