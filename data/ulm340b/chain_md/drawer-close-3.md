
    Steps:  1. Put gripper on the front of the drawer  2. Push the drawer closed
    Before we can push the drawer closed, we need to line the gripper up on the front of the drawer. Because the gripper is angled, we need to line the gripper up vertically.
    - When the robot's gripper is not vertically aligned with the drawer, the robot should put gripper on drawer.
    Once the gripper is vertically lined up on the drawer, we can just push it closed.
    - When the robot's gripper is vertically aligned with the drawer, the robot should push drawer.

The task `button-press-side` requires the robot to press the button from the side.
To press the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push the button from the side
    Because this is "side", we just need to line up the gripper on the side. Line up the robot's gripper as viewed from the side.
    - When the robot's gripper is not horizontally aligned with button, the robot should put gripper on button.
    Now that the gripper is lined up, just press the button from the side.
    - When the robot's gripper is horizontally aligned with button, the robot should push button from side.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Drop the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not above the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't dropped in the hole, drop the peg into the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not below the gripper, the robot should drop peg into hole.

The task