
If the robot's gripper is almost lined up as viewed from above, it can push on the button to try to turn the machine on. If the gripper is not almost lined up as viewed from above, it should move the gripper above the button.
    - When the robot's gripper is not almost vertically aligned with button, the robot should put gripper above button.
    As long as the gripper is mostly lined up, the robot should just keep trying to push.
    - When the robot's gripper is almost vertically aligned with button, the robot should push down on button.

The task `peg-insert-front` requires the robot to insert the peg into the hole from the front.
To insert the peg into the hole from the front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg forwards into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the front, insert it.
    - When peg is vertically aligned with hole, the robot should insert peg into hole.

The task `door-close` requires the robot to pull the door closed.
To pull the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull the door closed
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the