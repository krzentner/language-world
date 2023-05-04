
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    We need to put the gripper above the door handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle, the robot should put gripper around door handle.
    Once the gripper is around the door handle, we can just pull the door open.
    - When the robot's gripper is around door handle, the robot should pull away from door.

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Align the peg with the hole  4. Drop the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not aligned with hole, the robot should align peg to hole.
    If the peg is aligned with the hole, drop it into the hole.
    - When the peg is aligned with the hole, the robot should drop the peg into the hole.

The task `pick-place-side` requires the robot to pick up the peg and put it next to the hole from the side.
To pick up the peg and put it next to the hole from the side reliably, what steps the robot should perform?
    Steps