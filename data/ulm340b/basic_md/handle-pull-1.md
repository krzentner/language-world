
    - When the robot's gripper is not near the handle, the robot should grab handle.
    - When the robot's gripper is near the handle and the robot's gripper is not forward aligned with the handle, the robot should align gripper to handle.
    - When the robot's gripper is forward aligned with the handle and the robot's gripper is not left of the handle, the robot should drop gripper to handle.
    - When the robot's gripper is left of the handle, the robot should push up on handle.

The task `handle-press` requires the robot to press down the handle.
To press down the handle reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the handle, the robot should grab handle.
    - When the robot's gripper is near the handle and the robot's gripper is not forward aligned with the handle, the robot should align gripper to handle.
    - When the robot's gripper is forward aligned with the handle and the robot's gripper is not right of the handle, the robot should drop gripper to handle.
    - When the robot's gripper is right of the handle, the robot should push down on handle.

The task `button-press-side` requires the robot to push the button sideways.
To push the button sideways reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not left of button, the robot should put gripper to button.
    - When the robot's gripper is left of button and the robot's gripper is not touching button, the robot should drop gripper into button.
    - When the robot's gripper is touching button, the robot should push button right.

The task `button-press-top` requires the robot to press the button from the top.
To press the button from the top reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button and the robot's gripper is not right of button, the robot should drop gripper into button.
    - When the robot's gripper is right of button, the robot should push button left.

The task `button-press-side-v2` requires the robot to push the button sideways.
To push the button sideways reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not left