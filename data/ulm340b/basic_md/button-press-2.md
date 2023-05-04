

The task `pick` requires the robot to pick up the puck.
To pick up the puck reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot should push door closed.

The task `peg-unstack` requires the robot to lift the peg up.
To lift the peg up reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When peg is vertically aligned with the robot's gripper, the robot should lift peg off table.

The task `peg-insert` requires the robot to insert the peg into the hole.
To insert the peg into the hole reliably, the robot should perform the following steps:
    - When peg is vertically aligned with the robot's gripper and the peg is below the robot's gripper, the robot should drop peg into hole.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?

The task `pick-out-of-hole` requires the robot to pick up the peg from the hole.
To pick up the peg from the hole reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with peg, the robot should move gripper to left of peg.
    - When the robot's gripper is almost vertically aligned with peg, the robot should grab peg.

The task `insert-into-hole` requires the robot