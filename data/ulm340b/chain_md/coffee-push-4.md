

The task `coffee-push` requires the robot to grab the mug and move it to the target location.
To grab the mug and move it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above mug  2. Drop gripper around mug  3. Close gripper around mug  4. Move mug to goal
    First, put the gripper roughly above mug, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above mug, the robot should put gripper above mug.
    If the gripper isn't around the mug, put it around the mug.
    - When the robot's gripper is not around mug and the robot's gripper is open, the robot should put gripper around mug.
    If the gripper is near the mug and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near mug and the robot's gripper is open, the robot should close gripper around mug.
    We closed the gripper, and the mug is still near the gripper, so maybe we grabbed it. Try to move the mug to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above mug and the robot's gripper is closed, the robot should place mug at goal.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near door handle  2. Push door closed
    First, put the gripper somewhere near the door handle.
    - When the robot's gripper is not near door handle, the robot should grab door handle.
    If the robot's gripper is lined up with the door handle when viewed from the front, it is probably pushing the door closed.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `door-open-wall` requires the robot to pull the door open while keeping the wall aligned.
To pull the door open while keeping the wall aligned reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not vertically aligned with door handle, the robot should put