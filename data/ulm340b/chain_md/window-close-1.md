
    Steps:  1. Put gripper right of the window handle  2. Start pushing against the window handle to open the window  3. Push the window open harder
    If the robot's gripper is not vertically lined up with the window handle, we should move the gripper near the window handle to start pushing
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    If the robot's gripper is near the window handle we can probably slide the window open now by moving the gripper left.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.

The task `door-close` requires the robot to pull the door closed.
To pull the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    As long as the gripper is still vertically aligned with the door handle, it's being closed, so keep pulling.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door closed.

The task `button-press-side` requires the robot to press the button with its side.
To press the button with its side reliably, the robot should perform the following steps:
    Steps:  1. Move the robot's gripper to the left of the button  2. Move the robot's gripper against the left of the button  3. Press against the left of the button
    - When the robot's gripper is not left of the button, the robot should move gripper left of button.
    Make sure the gripper is near the button
    - When the robot's gripper is left of the button and the robot's gripper