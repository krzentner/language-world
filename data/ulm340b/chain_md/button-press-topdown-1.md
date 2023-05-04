
    What do you think?
    - When the robot's gripper is not above the button, the robot should put gripper above button.
    - When the robot's gripper is above the button and the robot's gripper is not near the button, the robot should move gripper to above button.
    - When the robot's gripper is above the button and the robot's gripper is near the button, the robot should press button.
    - When the robot's gripper is above the button and the robot's gripper is near the button, the robot should press button harder.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Lower the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole, insert it.
    - When peg is vertically aligned with hole, the robot should lower peg into hole.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
