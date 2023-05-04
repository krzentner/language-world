
    Steps:  1. Put gripper above button  2. Push down on the button from the top
    We don't want to press the button until it is lined up from the front. Line up the robot's gripper from the front.
    - When the robot's gripper is not near button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is forward aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button

The task `peg-unstack-side` requires the robot to unstack the peg and place it in the goal.
To unstack the peg and place it in the goal reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the top peg  2. Grab the top peg with the gripper  3. Slide the peg down sideways off the stack  4. Slide the peg into the hole
    Because we are unstacking the peg, put the gripper over the top peg in the stack.
    - When the robot's gripper is not above peg, move the robot's gripper until the robot's gripper is vertically aligned with peg
    If peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above peg
    If the peg is lined up with the hole to the side, insert it.
    - When the robot's gripper is forward aligned with peg and peg is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is horizontally aligned with hole

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2.