
To complete the task, the robot should perform the following steps:
    Steps:  1. Put gripper above button  2. Push down on the button
    Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `button-press` requires the robot to push the button.
To push the button reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above button  2. Line up the gripper from the front  3. Push the button in from the front
    Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up from above, make sure it's also lined up from the front.
    - When the robot's gripper is vertically aligned with button and the robot's gripper is not forward aligned with button, the robot should line up gripper with button.
    Once the gripper is lined up from the front, push in the button.
    - When the robot's gripper is forward aligned with button, the robot should push button in.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `push-back` requires the robot to push the puck to the target location.
To push the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push puck to goal
    First, put the gripper roughly above puck, so that we don'