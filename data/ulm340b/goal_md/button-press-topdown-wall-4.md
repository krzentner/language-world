
The robot should first make sure it is close to the button horizontally. Then it should line up the robot's gripper vertically above the button. Next, the robot should close its gripper until it is near the button.





The task `peg-insert-front` requires the robot to grab the peg and insert it into the hole from the front.
To grab the peg and insert it into the hole from the front reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg forwards into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the peg is horizontally aligned with the hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is lined up with the hole in the front, insert it.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole, move the robot's gripper until the robot's gripper is horizontally aligned with the hole

The task `drawer-close-wall` requires the robot to push the drawer closed with a short wall in the way.
To push the drawer closed with a short wall in the way reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot