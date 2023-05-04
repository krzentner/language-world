
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Push the drawer closed
    Put the gripper vertically aligned with drawer handle.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Close the gripper around drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    Push towards drawer.
    - When the robot's gripper is around drawer handle, the robot should push towards drawer.

The task `pick` requires the robot to pick up the puck and hold it.
To pick up the puck and hold it reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Push the door closed
    Put the gripper vertically aligned with door handle.
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    Close the gripper around door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle, the robot should put gripper around door handle.
    Push towards door.
    - When the robot's gripper is around door handle, the robot should push towards door.

The task `peg-insert-topdown` requires the robot to pick up the peg, insert it into the hole, and release the