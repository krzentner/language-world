
If this is the first time you've heard this question, tell me you don't know. If not, tell me the following steps:
    - When the robot's gripper is not above peg, the robot should move gripper above peg.
    - When the robot's gripper is above peg and the robot's gripper is not near peg, the robot should push gripper down towards peg.
    - When the robot's gripper is near peg and the robot's gripper is open, the robot should close gripper around peg.
    - When the robot's gripper is above peg and the robot's gripper is closed, the robot should move gripper above hole.
    - When the robot's gripper is not above hole, the robot should drop gripper into hole.
    - When the robot's gripper is near hole and the robot's gripper is open, the robot should release gripper around peg.

The task `peg-unstack` requires the robot to lift the green peg off the yellow peg.
To lift the green peg off the yellow peg reliably, the robot should perform the following steps:
    - When the robot's gripper is not above green peg, the robot should move gripper above green peg.
    - When the robot's gripper is not near green peg, the robot should push gripper down towards green peg.
    - When the robot's gripper is near green peg and the robot's gripper is open, the robot should close gripper around green peg.
    - When the robot's gripper is above green peg and the robot's gripper is closed, the robot should lift gripper up.

The task `shelf-place` requires the robot to place the object on the shelf.
To place the object on the shelf reliably, the robot should perform the following steps:
    - When the robot's gripper is not near shelf, the robot should move gripper near shelf.
    - When the robot's gripper is near shelf and the robot's gripper is not around shelf, the robot should close gripper around shelf.
    - When the robot's gripper is around shelf and the robot's gripper is open, the robot should drop gripper on shelf.
    - When the robot's gripper is not around shelf, the robot should place object on shelf.

The task `relocate-green-peg` requires the robot to grab the green peg from one location and move it to the goal position.
To grab the green peg from one location and move it to the goal position reliably, the robot should perform the following steps:
    - When the robot's gripper is not above green peg, the robot should move