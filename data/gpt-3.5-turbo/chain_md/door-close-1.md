The task `door-close` requires the robot to push the door closed to the target location.
To push the door closed to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed towards the target
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, the robot should move the gripper towards the door handle.
    If the door is aligned with the gripper as seen from in front, we can push the door towards the target location.
    - When the robot's gripper is forward aligned with the door handle and the robot's gripper is around door handle, the robot should push the door towards the target location.