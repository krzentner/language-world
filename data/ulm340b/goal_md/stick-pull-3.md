

The task `stick-push` requires the robot to grab the stick and use it to push the thermos to the target location.
To grab the stick and use it to push the thermos to the target location reliably, what steps the robot should perform?

The task `thermos-pick` requires the robot to grab the thermos and move it to the target location.
To grab the thermos and move it to the target location reliably, what steps the robot should perform?

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push the button
    Because we need to press the button from the side, make sure the gripper is horizontally aligned with button.
    - When the robot's gripper is not horizontally aligned with button, move the robot's gripper until the robot's gripper is horizontally aligned with button and the robot's gripper is closed
    As long as the gripper is still lined up, push the button.
    - When the robot's gripper is horizontally aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the