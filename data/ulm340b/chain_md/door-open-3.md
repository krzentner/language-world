
    Steps:  1. Put gripper above door handle  2. Grab door handle  3. Pull door open
    We need to put the gripper above the door handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    Once the gripper is lined up above the door handle, we should be able to grab the door handle by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle, the robot should put gripper around door handle.
    Once the gripper is around the door handle, we can just pull the door open.
    - When the robot's gripper is around door handle, the robot should pull away from door.

The task `door-close` requires the robot to push the door close.
To push the door close reliably, what steps the robot should perform?
    Steps:  1. Put gripper roughly around the door handle  2. Push the door closed
    If the gripper is not near the door handle, move it to the door handle. We don't need to be careful about the direction, since the door is large and we're just pushing it (unlike when opening the door).
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
    If the door is aligned with the gripper as seen from in front, we can push the door closed.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `push-turn` requires the robot to push the puck to the target location after turning on the spot.
To push the puck to the target location after turning on the spot reliably, the robot should perform the following steps:
    Steps:  1. Push the puck to the target location
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not