

To slide the plate back sideways into the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the plate and the plate is right of the robot's gripper, the robot should move gripper near plate.
    - When the robot's gripper is near the plate and the plate is right of the robot's gripper, the robot should move gripper behind plate.
    - When the robot's gripper is behind the plate, the robot should slide plate left.

The task `knob-turn-cw` requires the robot to rotate the knob clockwise.
To rotate the knob clockwise reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the knob and the knob is left of the robot's gripper, the robot should grab knob.
    - When the robot's gripper is near the knob and the robot's gripper is not forward aligned with the knob, the robot should align gripper with knob.
    - When the robot's gripper is forward aligned with the knob, the robot should turn knob clockwise.

The task `knob-turn-ccw` requires the robot to rotate the knob counterclockwise.
To rotate the knob counterclockwise reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the knob and the knob is left of the robot's gripper, the robot should grab knob.
    - When the robot's gripper is near the knob and the robot's gripper is not forward aligned with the knob, the robot should align gripper with knob.
    - When the robot's gripper is forward aligned with the knob, the robot should turn knob counterclockwise.

The task `lever-pull` requires the robot to pull the lever down.
To pull the lever down reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the handle and the handle is not below the robot's gripper, the robot should align gripper with handle.
    - When the robot's gripper is near the handle and the robot's gripper is not around the handle, the robot should put gripper around the handle.
    - When the robot's gripper is around the handle, the robot should pull the lever.

The task `handle-pull` requires the robot to pull the handle up.
To pull the handle up reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the handle, the robot should place gripper above handle.
    - When the robot's gripper is above the handle and the robot's gripper is not near the handle