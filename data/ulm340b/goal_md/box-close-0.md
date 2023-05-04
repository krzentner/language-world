
    No instruction provided.

The task `button-press-side` requires the robot to push the button down from the side.
To push the button down from the side reliably, what steps the robot should perform?
    No instruction provided.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, what steps the robot should perform?
    No instruction provided.

The task `pick` requires the robot to pick up the peg.
To pick up the peg reliably, what steps the robot should perform?
    No instruction provided.

The task `peg-insert-side-v2` requires the robot to grab the peg and insert it into the hole from the side.
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

The task `button-press-topdown-v2` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1.