
    Steps:  1. Move the gripper to the target location
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the button  2. Grab the button  3. Push in button  4. Retract gripper
    First, put the gripper above the button.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button
    If the button becomes left of the gripper, go back to putting the gripper above the button. Because the button is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When button is not left of the robot's gripper and button is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the button and the robot's gripper is closed
    If the button is aligned with the gripper as seen from in front, we can push the button.
    - When the robot's gripper is near the button and the button is in front of the robot's gripper, move the robot's gripper until the robot's gripper is above the button

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, move the robot's gripper until the robot's gripper is around the door handle
""".strip