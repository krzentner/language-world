
    - When the robot's gripper is not above drawer handle, the robot should put gripper above drawer handle.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should move gripper vertically aligned with drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle, the robot should push the drawer close.

The task `button-press-side` requires the robot to push the button down from the side.
To push the button down from the side reliably, what steps the robot should perform?
    - When the robot's gripper is not above the button, the robot should put the gripper above the button.
    - When the robot's gripper is left of the button and is horizontally aligned with button, the robot should put the gripper horizontally aligned with button.
    - When the robot's gripper is horizontally aligned with button, the robot should push the button left.

The task `button-press-longside` requires the robot to press the button all the way down from the side.
To press the button all the way down from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not above button, the robot should put gripper above button.
    - When the robot's gripper is left of button and the robot's gripper is horizontally aligned with button, the robot should put gripper horizontally aligned with button.
    - When the robot's gripper is near button and is horizontally aligned with button, the robot should push button left.
    - When the robot's gripper is in front of button, the robot should push button left harder.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the door handle, the robot should put gripper above door handle.
    -