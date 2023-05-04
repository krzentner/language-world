

To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the drawer handle  2. Drop the gripper around the drawer handle  3. Pull the drawer open
    First, put the gripper roughly above the drawer handle.
    - When the robot's gripper is not above the drawer handle, the robot should put gripper above drawer handle.
    As long as the gripper is above the drawer handle and open, dropping it closed should line it up the rest of the way.
    - When the robot's gripper is above the drawer handle and the robot's gripper is open, the robot should put gripper around drawer handle.
    As long as the gripper is vertically aligned with the drawer handle, it's being opened, so keep pulling.
    - When the robot's gripper is vertically aligned with the drawer handle, the robot should pull drawer open.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?

To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the side, insert it.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `button-press-side` requires the robot to push the button sideways.
To push the button sideways reliably,