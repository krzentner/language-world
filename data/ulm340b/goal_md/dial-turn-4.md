
Steps:  1. Put gripper above dial  2. Grab the dial  3. Turn the dial
    First, put the gripper above the dial.
    - When the robot's gripper is not above dial, move the robot's gripper until the robot's gripper is above the dial
    When the gripper is above the dial, move it down and to the side to grab the dial.
    - When the robot's gripper is above the dial and the robot's gripper is not near dial, move the robot's gripper until the robot's gripper is near the dial and the robot's gripper is closed
    Finally, turn the dial.
    - When the robot's gripper is around the dial, move the robot's gripper until the robot's gripper is horizontally aligned with the dial


The task `button-press-side` requires the robot to push the button down from the side.
To push the button down from the side reliably, what steps the robot should perform?
Steps:  1. Move the gripper to the button  2. Press down on the button from the side
    Because this is "side", we don't need to carefully line the gripper up. Just move it to the button.
    - When the robot's gripper is not near the button, move the robot's gripper until the robot's gripper is near the button
    If the gripper is near the button, push the button to turn it on.
    - When the robot's gripper is near the button, move the robot's gripper until the robot's gripper is almost vertically aligned with the button


The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `