
    Steps:

The task `window-close-topdown` requires the robot to slide the window closed to the right from above.
To slide the window closed to the right from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with the window handle, the robot should put the gripper above the window handle.
    If the robot's gripper is vertically aligned with the window handle and near the window handle, we should start pushing to close the window.
    - When the robot's gripper is vertically aligned with the window handle and the robot's gripper is near the window handle, the robot should slide window right.
    If the robot's gripper is now right of the window handle, we should push window right harder.
    - When the robot's gripper is right of the window handle, the robot should push window right harder.

The task `peg-insert-side-v1` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above peg  2. Grab peg with gripper  3. Line peg up with hole  4. Insert peg into hole
    First, put the gripper above the peg.
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the side, insert it.
    - When peg is horizontally aligned with hole, the robot should insert