
    Your goal is to help the robot learn a task plan by telling it what it should do in different situations. You can say what the robot should do, or ask for more examples. To say what the robot should do, press `say` and type it into the text box, like "If the robot's gripper is not above the object, the robot should place gripper above object". Press `submit`. To ask for more examples, press `ask`.

The task `peg-insert-front` requires the robot to grab the peg and insert it into the hole in front.
To grab the peg and insert it into the hole in front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Align peg with the hole  4. Push the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the front, insert it.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Align peg with the hole  4. Drop the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object