
    - When robot's gripper is not vertically aligned with handle and robot's gripper is not near handle, robot should put gripper above handle.
    - When robot's gripper is almost aligned with handle and robot's gripper is open, robot should put gripper around handle.
    - When robot's gripper is near handle, robot should pull handle.

The task `peg-unplug-side` requires the robot to unplug the peg from the hole from the side.
To unplug the peg from the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with peg, the robot should pull peg out of hole.

The task `button-press-side` requires the robot to push the button with the robot's gripper from the side.
To push the button with the robot's gripper from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When button is not left of the robot's gripper and button is not forward aligned with the robot's gripper, the robot should grab button.
    - When the robot's gripper is forward aligned with button, the robot should push button.

The task `peg-insert-sideway` requires the robot to grab the peg and insert it into the hole.
To grab the peg and insert it into the hole reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg and the robot's gripper is below the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg, the robot should insert peg into hole.

The task `peg-unplug-sideway` requires the robot to unplug the peg from the hole.
To unplug the peg from the hole reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg and the robot's gripper is below the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with