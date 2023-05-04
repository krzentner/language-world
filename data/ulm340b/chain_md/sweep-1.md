
Steps:  1. Put gripper above cube  2. Put gripper around cube  3. Close gripper around cube  4. Slide cube to goal
First, put the gripper above cube, so that we don't bump it while trying to grab it.
- When the robot's gripper is not above cube, the robot should put gripper above cube.
If the gripper isn't around the cube, put it around the cube.
- When the robot's gripper is not around cube, the robot should put gripper around cube.
If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
- When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
As long the gripper is still mostly around the cube, we can slide the cube to the goal.
- When the robot's gripper is forward aligned with cube, the robot should slide cube to goal.

The task `pick-hollow-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?
Steps:  1. Move the robot's gripper above the puck  2. Drop the robot's gripper around the puck  3. Close the robot's gripper around the puck  4. Move the puck to the goal
First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
- When the robot's gripper is not above puck, the robot should place gripper above puck.
If the gripper isn't around the puck, put it around the puck.
- When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
- When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to move the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
- When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the