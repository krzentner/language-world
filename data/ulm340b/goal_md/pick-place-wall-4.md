
`pick-place-wall` is similar to `pick-place` because it involves the robot picking up a puck and holding it somewhere.
`pick-place-wall` is different to `pick-place` because there is a short wall in the way.


This task is similar to:
- Window Close
- Button Press Topdown

This task is different from:
- Button Press
- Door Open
- Reach


Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above puck and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location with a short wall in the way.
To pick up the puck and hold it at the target location with a short wall in the way reliably, what steps the robot should perform?
`pick-place-wall` is similar to `pick-place` because it involves the robot picking up a puck and holding it somewhere.
`pick-place-wall` is different to `pick-place` because there is a short wall in the way.


This task is similar to:
- Window Close
- Button Press Topdown

This task is different from:
- Button Press
- Door Open
- Reach

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location