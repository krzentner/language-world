

1. When the robot's gripper is not near puck, the robot should put the gripper above the puck.
2. When the robot's gripper is near puck, the robot should pick up puck.
3. When the robot's gripper is not above puck hold target, the robot should reach to puck hold target.

The task `slide-cover-left` requires the robot to slide the cover open to the left.
To slide the cover open to the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not near cover, the robot should put the gripper above cover.
    - When the robot's gripper is above cover and the robot's gripper is not right of cover, the robot should slide cover left.
    - When the robot's gripper is right of cover, the robot should pull cover left.

The task `slide-cover-right` requires the robot to slide the cover closed to the right.
To slide the cover closed to the right reliably, the robot should perform the following steps:
    - When the robot's gripper is not near cover, the robot should put the gripper above cover.
    - When the robot's gripper is above cover and the robot's gripper is not left of cover, the robot should slide cover right.
    - When the robot's gripper is left of cover, the robot should pull cover right.

The task `drawer-close-w-obstacle` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should move the gripper above the drawer handle.
    - When the robot's gripper is not near the drawer handle, the robot should grab the drawer handle.
    - When the robot's gripper is near the drawer handle, the robot should push the drawer closed.

The task `door-open-w-obstacle` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the door handle, the robot should move the gripper above the door handle.
    - When the robot's gripper is not near the door handle, the robot should put the gripper around the door handle.
    - When the robot's gripper is around the door handle, the robot should pull the door open.

The task `button-press-side` requires the robot to push the button down from the side.
To push the button down from the side reliably, the robot should perform the following steps:
    -