
Steps:  1. Put gripper above handle  2. Drop gripper around handle  3. Pull the handle up
First, put the gripper above the handle.
- When the robot's gripper is not vertically aligned with handle, move the robot's gripper until the robot's gripper is vertically aligned with the handle
If the robot's gripper is not around the handle, move it down around it to grab the handle.
- When the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle, move the robot's gripper until the robot's gripper is around the handle
If the robot's gripper is around the handle, we can pull it up now.
- When the robot's gripper is around handle, move the robot's gripper until the robot's gripper is left of the handle

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is lined up with the hole to the side, insert it.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is horizontally aligned with hole

The task `door-close` requires the robot to push