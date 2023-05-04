
    Steps:  1. Reach around the wall to the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.

The task `reach-over-wall` requires the robot to reach to the target location over a short wall.
To reach to the target location over a short wall reliably, what steps the robot should perform?
    Steps:  1. Reach over the wall to the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.

The task `push-wall` requires the robot to slide the puck to the target location with a short wall in the way.
To slide the puck to the target location with a short wall in the way reliably, what steps the robot should perform?
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location with a short wall in the way.
To pick up the puck and hold it at the target location with a short wall in the way reliably, what steps the robot should perform?
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4