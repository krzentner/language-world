
First, put the gripper roughly around the drawer handle.
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    As long as the gripper is in front of the drawer handle, we can pull it open.
    - When the robot's gripper is not around the drawer handle and the robot's gripper is in front of the drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle.
    - When the robot's gripper is not near the door handle, move the robot's gripper until the robot's gripper is near the door handle
    As long as the gripper is around the door handle, we can push the door closed.
    - When the robot's gripper is not around the door handle and the robot's gripper is near the door handle, move the robot's gripper until the robot's gripper is around the door handle

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is lined up with the hole to the side, insert it