
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways out of the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the side, slide it out.
    - When peg is horizontally aligned with hole, the robot should remove peg from hole.

The task `pick-out-of-hole` requires the robot to pick up the puck out of the hole.
To pick up the puck out of the hole reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the puck  2. Grab the puck with the gripper  3. Lift the puck straight up  4. Move the puck up a bit
    First, put the gripper above the puck.
    - When the robot's gripper is not vertically aligned with the puck, the robot should put gripper above puck.
    If the puck becomes left of the gripper, go back to putting the gripper above the puck. Because the puck is a small object, we should check if the gripper is lined up with it by looking if it's around it, instead of from the front.
    - When puck is not left of the robot's gripper and puck is not around robot's gripper, the robot should grab puck.
    If the puck is below the gripper but the gripper is still lined up with it, try to lift it up.
    - When the robot's gripper is still vertically aligned with the puck and the puck is not near robot's gripper, the robot should lift puck up.
    If the puck is above the gripper, move it up a little to finish removing it from the hole.
    