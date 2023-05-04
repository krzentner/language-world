

The task `button-press-bottomup` requires the robot to push the button up from below.
To push the button up from below reliably, the robot should perform the following steps:
    - When the robot's gripper is below button and the robot's gripper is not vertically aligned with button, the robot should move the gripper left of button.
    - When the robot's gripper is below button and the robot's gripper is vertically aligned with button, the robot should push button up.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with door handle, the robot should put the gripper above door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is open, the robot should put the gripper around door handle.
    - When the robot's gripper is vertically aligned with door handle, the robot should push door closed.

The task `peg-unplug-side` requires the robot to remove the peg from the hole by pulling it out from the side.
To remove the peg from the hole by pulling it out from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with peg, the robot should put gripper to left of peg.
    - When peg is forward aligned with robot's gripper and peg is vertically aligned with robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should pull peg out of hole.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not above peg, the robot should move gripper above peg.
    - When the robot's gripper is above peg and the robot's gripper is open, the robot should drop gripper around peg.
    - When peg is forward aligned with robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with the hole, the robot should align peg to hole.
    - When peg is vertically aligned with hole, the robot should insert peg into hole.

The task `peg-insert-side` requires the