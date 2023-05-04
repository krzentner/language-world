
     Steps: 1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the robot's gripper is not near the window handle, we should move it to the window handle to start pushing it.
    - When the robot's gripper is vertically aligned with the window handle, move the robot's gripper until the robot's gripper is near the window handle
    If the robot's gripper is in front of the window handle, we can start pushing the window closed by moving the gripper right.
    - When the robot's gripper is vertically aligned with the window handle and the robot's gripper is not in front of the window handle, move the robot's gripper until the robot's gripper is in front of the window handle
    If the robot's gripper is around the window handle, push the window harder to close it.
    - When the robot's gripper is around the window handle, move the robot's gripper until the robot's gripper is vertically aligned with the window handle

The task `button-press-side` requires the robot to press the button by pushing sideways on it.
To press the button by pushing sideways on it reliably, the robot should perform the following steps:
     Steps: 1. Put gripper above the button  2. Drop gripper around button  3. Slide the gripper sideways into the button
    First, put the gripper above the button.
    - When the robot's gripper is not above the button, move the robot's gripper until the robot's gripper is above the button
    If the gripper is above the button and not around the button, we should try putting the gripper around the button.
    - When the robot's gripper is above the button and the robot's gripper is not around the button, move the robot's gripper until the robot's gripper is around the button
    If the gripper is around the button, slide it sideways into the button to press it.
    - When the robot's gripper is around the button and the robot's gripper is not left of the button, move the robot's gripper until the robot's gripper is left of the button

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because