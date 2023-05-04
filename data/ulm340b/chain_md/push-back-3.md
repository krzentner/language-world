
    Steps:  1. Put gripper above puck  2. Push gripper into puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `pick-place-back` requires the robot to pick up the puck and place it at the target location.
To pick up the puck and place it at the target location reliably, what steps the robot should perform?
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to move the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should