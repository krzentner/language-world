
    We need to put the gripper above the door handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle, the robot should put gripper around door handle.
    Once the gripper is around the door handle, we can just pull the door open.
    - When the robot's gripper is around door handle, the robot should pull away from door.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    If the robot's gripper is near the window handle we can probably slide the window close now by moving the gripper right.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is starting to be in front of the window handle, push harder.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?
    We don't have any objects to manipulate, so we can just move the robot's gripper directly