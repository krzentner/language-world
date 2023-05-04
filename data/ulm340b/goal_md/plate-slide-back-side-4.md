
    Steps:  1. Put gripper in front of the plate  2. Push the plate toward the target location
    If the robot's gripper is not near the plate we should move the gripper near the plate to start pushing
    - When the robot's gripper is not near the plate, move the robot's gripper until the robot's gripper is near the plate
    If the robot's gripper is in front of the plate we can probably slide the plate toward the target location now by moving the gripper to the side.
    - When the robot's gripper is left of the plate, move the robot's gripper until the robot's gripper is forward aligned with the plate

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg downward into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is lined up with the hole above, insert it.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is vertically aligned with hole

"""

[eod] [code]from datetime import timedelta


class Timer(object):
    def __init__(self):
        self._end_time = None

    def start(self, td):
        self