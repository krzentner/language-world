

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around the door handle  2. Push the door closed
    We need to put the gripper around the door handle before we can push the door closed.
    - When the robot's gripper is not around the door handle, move the robot's gripper until the robot's gripper is around the door handle
    Once the gripper is around the door handle, we can just push the door closed.
    - When the robot's gripper is around the door handle, move the robot's gripper until the robot's gripper is almost horizontally aligned with the door handle

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Drop the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not above the peg and the robot's gripper is closed, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When the robot's gripper is open and peg is not left of the robot's gripper, move the robot's gripper until the robot's gripper is left of the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole and the robot's gripper is near peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg and the robot's gripper is closed
    If the peg is aligned with the hole and near it, try inserting it.
    - When peg is above hole, move the robot's gripper until the robot's gripper is near peg

The task `button-press-side` requires the robot to press the button sideways from above.
To press the button sideways from above reliably, the robot