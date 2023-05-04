
     Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.


The task `slide-lock-left` requires the robot to slide the puck against the left lock to open the door.
To slide the puck against the left lock to open the door reliably, the robot should perform the following steps:
    Steps:  1. Slide puck close to the left lock  2. Push puck left towards the lock  3. Push the puck harder against the left lock to open the door
    If the gripper isn't above the puck, it needs to move there.
    - When the robot's gripper is not above puck, the robot should move the gripper above the puck.
    Once the robot's gripper is above the puck, it should start sliding towards the lock.
    - When the robot's gripper is above puck, the robot should move puck towards lock.
    If the gripper is at the left of the lock, try pushing the puck against it.
    - When the gripper is left of the left lock, the robot should push puck against left lock.

The task `slide-lock-right` requires the robot to slide the puck against the right lock to open the door.
To slide the puck against the right lock to open the door reliably, the robot should perform the following steps:
    Steps:  1. Slide puck close to the right lock  2. Push puck right towards the lock  3. Push the puck harder against the right lock to open the door
    If the gripper isn