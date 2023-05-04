

    - When the robot's gripper is not almost vertically aligned with button and button is not near robot's gripper, the robot should move gripper above button.
    - When the button is almost vertically aligned with the robot's gripper and the robot's gripper is not near button, the robot should push button down.

The task `pick` requires the robot to pick up the peg.
To pick up the peg reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    - When peg is near the robot's gripper and the robot's gripper is open, the robot should grab peg.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not near door handle, the robot should push door handle closed.

The task `peg-unplug-side` requires the robot to grab the peg and lift it out of the hole from the side.
To grab the peg and lift it out of the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is vertically aligned with hole, the robot should lift peg from hole.

The task `stack` requires the robot to pick up the puck and place it on top of the small cylinder.
To pick up the puck and place it on top of the small cylinder reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should