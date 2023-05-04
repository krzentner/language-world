

The task `drawer-close-topdown` requires the robot to close the drawer from above.
To close the drawer from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Push drawer closed
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    Once the gripper is around the drawer handle, we can just push the drawer closed.
    - When the robot's gripper is around drawer handle, the robot should push drawer closed.

The task `door-close-topdown` requires the robot to close the door from above.
To close the door from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull door closed
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    As long as the gripper is still vertically aligned with the door handle, we're closing it, so keep pulling.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door closed.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?

The task `pick-place-side` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck