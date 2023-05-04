Please choose all that apply.
    - When the robot's gripper is not vertically aligned with the handle, the robot should put gripper above handle.
    - When the robot's gripper is right of handle and robot's gripper is open, the robot should put gripper around handle.
    - When the robot's gripper is vertically aligned with handle, the robot should pull up on handle.

The task `door-close` requires the robot to pull the door closed.
To pull the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with door handle, the robot should push door closed.

The task `peg-unplug-side` requires the robot to unplug the peg from the hole and place it on the table.
To unplug the peg from the hole and place it on the table reliably, the robot should perform the following steps:
    - When the robot's gripper is not above peg, the robot should move gripper above peg.
    - When the robot's gripper is above peg and the robot's gripper is open, the robot should grab peg.
    - When the robot's gripper is forward aligned with peg and the robot's gripper is closed, the robot should pull peg from hole.
    - When the robot's gripper is forward aligned with peg and the robot's gripper is closed, the robot should drop peg on table.

The task `button-press-side` requires the robot to push the button to the left.
To push the button to the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with the button and the button is not left of the robot's gripper, the robot should move gripper above button.
    - When the robot's gripper is horizontally aligned with button and the robot's gripper is open, the robot should grab button.
    - When the robot's gripper is forward aligned with button and the robot's gripper is closed, the robot should push button left.
    - When the robot's gripper is forward aligned with button and the robot's gripper is closed, the robot should push button harder.

The task `slider-push` requires the robot to slide the button to the right.
To slide the button to the right reliably, the robot should perform the following steps:
    - When