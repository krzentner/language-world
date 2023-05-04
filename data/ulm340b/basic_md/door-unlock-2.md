
    - When the robot's gripper is not around the door knob, the robot should grab door knob.
    - When the robot's gripper is forward aligned with door knob and the robot's gripper is closed, the robot should turn door knob.
    - When the dial is to the left of the green mark on the door, the robot should turn dial right.
    - When the dial is right of the green mark on the door, the robot should turn dial left.
    - When the dial is at the green mark on the door, the robot should release door knob.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg and the robot's gripper is not above the peg, the robot should put gripper above peg.
    - When the robot's gripper is not around the peg, the robot should grab peg.
    - When the robot's gripper is around the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not left of button and the robot's gripper is not forward aligned with button, the robot should grab button.
    - When the robot's gripper is forward aligned with button and the robot's gripper is closed, the robot should push down on button.

The task `peg-unstack` requires the robot to pick up the top peg from a tower of two pegs.
To pick up the top peg from a tower of two pegs reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the top peg and the robot's gripper is not vertically aligned with the top peg, the robot should move gripper above top peg.
    - When the robot's gripper is vertically aligned with the top peg and the robot's gripper is not around the top peg, the robot should put gripper around top peg.
    - When the robot's gripper is around top peg, the robot should pull top peg up.

The task `push-middle` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    - When the robot