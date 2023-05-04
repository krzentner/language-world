
    - When the window handle is to the right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move the gripper to the left of the window handle.
    - When the robot's gripper is near the window handle, the robot should slide the window to the left.
    - When the robot's gripper is in front of the window handle, the robot should push the window to the left harder.

The task `receptacle-open` requires the robot to pull the receptacle open.
To pull the receptacle open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with receptacle handle, the robot should put gripper above receptacle handle.
    - When the robot's gripper is vertically aligned with the receptacle handle and the robot's gripper is not around receptacle handle, the robot should put gripper around receptacle handle.
    - When the robot's gripper is around receptacle handle, the robot should pull receptacle handle.

The task `peg-unstack` requires the robot to lift the small peg off the big peg.
To lift the small peg off the big peg reliably, the robot should perform the following steps:
    - When the robot's gripper is not above peg and the robot's gripper is not above the big peg, the robot should put the gripper above the small peg.
    - When the robot's gripper is above the small peg and the robot's gripper is not around the small peg, the robot should drop the gripper around the small peg.
    - When the robot's gripper is around the small peg and the gripper is above the big peg, the robot should lift the gripper.

The task `peg-stack` requires the robot to lift the small peg and hold it on the top of the big peg.
To lift the small peg and hold it on the top of the big peg reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the peg and the robot's gripper is not above the big peg, the robot should put the gripper above the small peg.
    - When the robot's gripper is above the small peg and the robot's gripper is not around the small peg, the robot should drop the gripper around the small peg.
    - When the robot's gripper is around the small peg and the gripper is above the big peg, the robot should place the small peg on top of the big peg.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from