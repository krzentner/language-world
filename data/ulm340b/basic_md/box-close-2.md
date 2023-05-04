


The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `window-open` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window left.
    - When the robot's gripper is in front of the window handle, the robot should push window left harder.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper,