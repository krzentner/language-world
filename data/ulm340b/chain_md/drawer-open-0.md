
    The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper below the drawer handle  2. Drop gripper around the drawer handle  3. Pull the drawer open
    First, put the gripper below the drawer handle.
    - When the robot's gripper is not below drawer handle, the robot should put gripper below drawer handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is below the drawer handle and the robot's gripper is open, the robot should put gripper around drawer handle.
    As long as the gripper is still below the drawer handle, it's being opened, so keep pulling.
    - When the robot's gripper is below drawer handle, the robot should pull drawer open.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near button  2. Push gripper against button
    If the gripper is not near button, move it closer.
    - When the robot's gripper is not near button, the robot should put gripper near button.
    As long as the gripper is close to the button, it should be able to just push the button sideways to press it.
    - When the robot's gripper is near button, the robot should push gripper against button.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Push the peg down into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg