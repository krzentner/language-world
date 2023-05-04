

    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with button, the robot should put gripper above button.
    - When the robot's gripper is horizontally aligned with button, the robot should push button sideways.

The task `button-press-topdown-short` requires the robot to push the button down from above with a short wall in the way.
To push the button down from above with a short wall in the way reliably, what steps the robot should perform?

    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `peg-insert-side-short` requires the robot to grab the peg and insert it into the hole from the side with a short wall in the way.
To grab the peg and insert it into the hole from the side with a short wall in the way reliably, what steps the robot should perform?

    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `reach-wall` requires the robot to reach to the target location with a short wall in the way.
To reach to the target location with a short wall in the way reliably, what steps the robot should perform?

    - When the robot's gripper is not near reach target, the robot should reach to goal.















"""

import sys
import random

