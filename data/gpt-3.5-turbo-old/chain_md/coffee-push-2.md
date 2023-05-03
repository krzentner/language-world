To grab the mug and move it to the target location reliably, the robot should perform the following steps:

Steps:  1. Put gripper above mug handle  2. Drop gripper around mug handle  3. Close gripper around mug handle  4. Move mug to goal
First, put the gripper roughly above the mug handle, so that we don't bump it while trying to grab it.
- When the robot's gripper is not above the mug handle, the robot should place gripper above the mug handle.
If the gripper isn't around the mug handle, put it around the mug handle.
- When the robot's gripper is not around the mug handle and the robot's gripper is open, the robot should drop gripper around the mug handle.
If the gripper is near the mug handle and open, maybe we can grab it by closing the gripper.
- When the robot's gripper is near the mug handle and the robot's gripper is open, the robot should close gripper around mug handle.
We closed the gripper, and the mug is still near the gripper, so maybe we grabbed it. Try to move the mug to the goal. If we didn't grab it, we'll just go back to an earlier step.
- When the robot's gripper is above the mug and the robot's gripper is closed, the robot should move the mug to the goal location.