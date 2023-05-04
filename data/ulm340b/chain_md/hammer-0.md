


The task `stick-push` requires the robot to push the stick to the target location.
To push the stick to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the stick  2. Put gripper roughly around the stick  3. Push the stick to the target location
    First, put the gripper above the stick.
    - When the robot's gripper is not above the stick, the robot should put gripper above stick.
    Now put the gripper around the stick. The robot should not line up the gripper around the stick carefully, so that the gripper doesn't miss the stick.
    - When the robot's gripper is not around stick, the robot should put gripper around stick.
    Now just push the stick towards the target location.
    - When the stick is not at the target location, the robot should push stick.

The task `pick-place-with-gripper` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to move the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `window-open-door-handle` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, the robot should perform the following steps:
    