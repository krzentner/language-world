
    Steps:  1. Put the gripper above the button  2. Close the gripper  3. Move forward until the gripper can press the button
    First, put the gripper above the button so that we don't hit the wall with the gripper when we try to close the gripper.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is above the button, we can close the gripper.
    - When the robot's gripper is vertically aligned with button and the robot's gripper is not near button, the robot should close gripper.
    Now that the gripper is close to the button, we can probably start pushing. Move forward so that the gripper can push the button.
    - When the robot's gripper is near button, the robot should push button.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    Steps:  1. Put the gripper in front of the button  2. Close the gripper  3. Move the gripper to the button
    First, put the gripper in front of the button so that we don't hit the wall with the gripper when we try to close the gripper.
    - When the robot's gripper is not horizontally aligned with button, the robot should put gripper in front of button.
    Now that the gripper is in front of the button, we can close the gripper.
    - When the robot's gripper is horizontally aligned with button and the robot's gripper is not near button, the robot should close gripper.
    Now that the gripper is close to the button, we can probably start pushing. Move the gripper to the button.
    - When the robot's gripper is near button, the robot should push button.

The task `button-press-bottomup` requires the robot to push the button from below.
To push the button from below reliably, what steps the robot should perform?
    Steps:  1. Line up the gripper as viewed from above  2. Push the gripper up to press the button
    Because this is "bottomup", we just need to line up the gripper from below. Line up the robot's gripper from below.
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not below button, the robot should put gripper below button.
    Now that the gripper