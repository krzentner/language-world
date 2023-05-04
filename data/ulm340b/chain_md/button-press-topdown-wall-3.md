

The task `pick-out-of-hole` requires the robot to pick the peg out of the hole.
To pick the peg out of the hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above peg  2. Grab peg with the gripper  3. Pull the peg out of the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    Grab the peg with the gripper by moving it around the peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    If the peg is forward aligned with the gripper but not near the gripper, pull it out of the hole.
    - When the robot's gripper is forward aligned with peg and the peg is not near the robot's gripper, the robot should pull peg out of the hole.

The task `button-press-side` requires the robot to push the button sideways.
To push the button sideways reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push the button from the side
    First, line up the robot's gripper with the button, as seen from the side.
    - When the robot's gripper is not horizontally aligned with button, the robot should align gripper with button.
    If the gripper is aligned with the button, push on it.
    - When the robot's gripper is horizontally aligned with button, the robot should push button to the right.

The task `sweeping` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck