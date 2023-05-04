
    Steps:  1. Line up the gripper as viewed from the front  2. Push the button from the front
    This is similar to the "topdown" version, but we need to line up the gripper as viewed from the front.
    - When the robot's gripper is not forward aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push the button.
    - When the robot's gripper is forward aligned with button, the robot should push down on button.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    Steps:  1. Put gripper above button  2. Drop gripper around button  3. Push button sideways
    First, put the robot's gripper above the button.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    If the button becomes left of the gripper, go back to putting the gripper above the button.
    - When button is not left of the robot's gripper and the robot's gripper is open, the robot should drop gripper around button.
    If the gripper is near the button, the button will probably get pushed sideways.
    - When the robot's gripper is near button, the robot should push button left.

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole vertically.
To grab the peg and insert it into the hole vertically reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Drop gripper around peg  3. Line the peg up with the hole  4. Push the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    If the peg is left of the gripper, go back to putting the gripper above the peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    If the robot's gripper is around the peg, it's safe to move the peg. Start by pushing it against the hole.
    - When the robot's gripper is forward aligned with peg and peg is not below hole, the robot should push peg up.
    Once the peg is