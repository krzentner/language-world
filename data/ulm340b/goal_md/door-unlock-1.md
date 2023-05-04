
    Steps:  1. Put gripper above the dial  2. Start moving the gripper to turn the dial
    It looks like the dial can be turned by moving the gripper right.
    - When the robot's gripper is above the dial and the robot's gripper is not near the dial, move the robot's gripper until the robot's gripper is near the dial
    To avoid bumping the door knob, first line up the gripper as viewed from above.
    - When the robot's gripper is not above the dial, move the robot's gripper until the robot's gripper is above the dial

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

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3.