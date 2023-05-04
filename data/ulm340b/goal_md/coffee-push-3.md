
    Steps:  1.  2.  3.  4.
    First, put the gripper above mug, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above mug, move the robot's gripper until the robot's gripper is above mug
    If the gripper isn't near the mug, put it around the mug.
    - When the robot's gripper is not near mug, move the robot's gripper until the robot's gripper is near mug
    Now that we're close to mug, close the gripper and probably pick up mug.
    - When the robot's gripper is above mug and the robot's gripper is open, move the robot's gripper until the robot's gripper is around mug and the robot's gripper is closed
    Now that we've probably picked up mug, move it to the target location.
    - When the robot's gripper is around mug, move the robot's gripper until the robot's gripper is near the target location

The task `button-press` requires the robot to push the button down from the side.
To push the button down from the side reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper to the right of button  2. Put gripper above button  3. Drop gripper around button  4. Push button
    First, put the gripper to the right of button, so that we don't bump it while trying to press it.
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not above button, move the robot's gripper until the robot's gripper is vertically aligned with button and the robot's gripper is above button
    Now that we're near button, put the gripper above button.
    - When the robot's gripper is not almost vertically aligned with button and the robot's gripper is not above button, move the robot's gripper until the robot's gripper is almost vertically aligned with button and the robot's gripper is above button
    If the gripper is above button, it should be easy to put the gripper around it.
    - When the robot's gripper is above button and the robot's gripper is not around button, move the robot's gripper until the robot's gripper is around button and the robot's gripper is closed
    If the robot's gripper is around button, we should be able to push