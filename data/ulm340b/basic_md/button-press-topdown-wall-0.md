

The task `button-press-side` requires the robot to push the button sideways.
To push the button sideways reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with button and the robot's gripper is not above the button, the robot should put gripper above button.
    - When the robot's gripper is forward aligned with button, the robot should push button in forward direction.

The task `peg-unplug-side` requires the robot to grab the peg from the side and lift it straight up and out of the hole by overcoming its friction.
To grab the peg from the side and lift it straight up and out of the hole by overcoming its friction reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is vertically aligned with the peg, the robot should pull peg up.

The task `peg-insert-side-start-in-hole` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `peg-unplug-side-start-in-hole` requires the robot to grab the peg from the side and lift it straight up and out of the hole by overcoming its friction.
To grab the peg from the side and lift it straight up and out of the hole by overcoming its friction reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is vertically aligned with the peg, the robot should pull peg up.

The task `door-close` requires the robot