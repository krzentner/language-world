
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck back to goal
    First, line up the gripper above the puck, so that we can trap it between the gripper and the ground.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should place gripper above puck.
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `push-grasp-push` requires the robot to trap the puck between its gripper and a flat surface in order to slide it to the target location.
To trap the puck between its gripper and a flat surface in order to slide it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper to surround puck  3. Push puck to goal
    First, line up the gripper above the puck, so that we can trap it between the gripper and the ground.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should place gripper above puck.
    If the gripper is lined up with the puck, move it down.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is open, the robot should drop gripper to surround puck.
    If the robot is near the puck and the gripper is closed, we can start pushing the puck.
    - When the robot's gripper is near puck and the robot's gripper is closed, the robot should push puck to goal.

The task `door-locked` requires the robot to turn the door handle clockwise in order to unlock the door.
To turn the door handle clockwise in order to unlock the door reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the door handle  2. Grab the door handle by moving the