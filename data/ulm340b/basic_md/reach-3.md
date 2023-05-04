

The task `peg-unplug-side` requires the robot to grab the peg and unplug it from the hole from the side.
To grab the peg and unplug it from the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not horizontally aligned with the peg and the robot's gripper is not left of the peg, the robot should put gripper next to peg.
    - When the robot's gripper is left of peg, the robot should grab peg.
    - When the robot's gripper is around peg, the robot should lift peg out of hole.
    - When the robot's gripper is horizontally aligned with peg and the peg is out of the hole, the robot should move gripper left of peg.

The task `peg-unplug-vertical` requires the robot to grab the peg and unplug it from the hole from above.
To grab the peg and unplug it from the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not above peg and the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When the robot's gripper is vertically aligned with peg, the robot should grab peg.
    - When the robot's gripper is above peg and the peg is out of the hole, the robot should move gripper away from peg.

The task `push-back` requires the robot to slide the puck backwards.
To slide the puck backwards reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with puck and the robot's gripper is not above puck, the robot should put the gripper above the puck.
    - When the robot's gripper is above the puck, the robot should slide the puck backwards.

The task `pick-out` requires the robot to pick the puck out of the cup.
To pick the puck out of the cup reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the puck and the robot's gripper is not above puck, the robot should put the gripper above the puck.
    - When the robot's gripper is above puck and the robot's gripper is not near puck, the robot should drop gripper into puck.
    - When the robot's gripper is near puck and the robot's gripper is not open, the robot should close gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should lift puck out of cup.
    - When the robot's gripper