

- put gripper in front of plate
- push plate away
- slide plate to goal

The task `plate-slide-side` requires the robot to slide the plate sideways into the target location.
To slide the plate sideways into the target location reliably, what steps the robot should perform?

- put gripper in front of plate
- push plate away
- slide plate to goal

The task `handle-press` requires the robot to press down the handle of the lever.
To press down the handle of the lever reliably, the robot should perform the following steps:
    - When the robot's gripper is above the handle, the robot should put gripper above handle.
    - When the robot's gripper is vertically aligned with the handle, the robot should put gripper around handle.
    - When the robot's gripper is around the handle, the robot should press down on handle.

The task `lever-pull` requires the robot to pull the lever.
To pull the lever reliably, the robot should perform the following steps:
    - When the robot's gripper is above lever handle and the robot's gripper is not vertically aligned with the lever handle, the robot should put gripper above lever handle.
    - When the robot's gripper is vertically aligned with the lever handle and the robot's gripper is not around lever handle, the robot should put gripper around lever handle.
    - When the robot's gripper is around the lever handle, the robot should pull lever.

The task `light-switch-side` requires the robot to flip the light switch up.
To flip the light switch up reliably, the robot should perform the following steps:
    - When the robot's gripper is above the light switch and the robot's gripper is above the upper half of the light switch, the robot should put gripper below light switch.
    - When the robot's gripper is below the light switch and the robot's gripper is below the lower half of the light switch, the robot should put gripper above light switch.
    - When the robot's gripper is below the upper half of the light switch and the robot's gripper is above the lower half of the light switch, the robot should flip light switch up.

The task `switch-press` requires the robot to press the switch.
To press the switch reliably, the robot should perform the following steps:
    - When the robot's gripper is vertically aligned with the switch, the robot should put gripper above switch.
    - When the robot's gripper is above switch and the robot's gripper is not around switch, the robot should put gripper around switch.
    - When the robot's gripper