
The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Align the gripper above the peg  2. Close the gripper around the peg  3. Put the peg in the hole, aligning the gripper with the hole as viewed from the side  4. Push the peg down into the hole
    Align the gripper above the peg first. Since the peg is long, we don't need to make sure it's not aligned sideways.
    - When the robot's gripper is not vertically aligned with peg, the robot should align gripper above peg.
    Once the gripper is above the peg, close the gripper around the peg to try to grab the peg.
    - When the robot's gripper is vertically aligned with peg and the robot's gripper is open, the robot should grab peg.
    Now that the robot's gripper is closed and near the peg, we might have grabbed the peg. If so, we can try to line up the peg with the hole, as seen from the side, to insert it.
    - When the robot's gripper is near peg and the robot's gripper is closed, the robot should line gripper up with hole.
    Once the gripper is near the hole, the peg will probably fall into the hole.
    - When the robot's gripper is in front of the hole, the robot should push the peg into the hole.

The task `door-close` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    As long as the gripper is still vertically aligned with the door handle, it's being opened, so keep pulling.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

The task `door-close` requires the