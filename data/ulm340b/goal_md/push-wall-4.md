
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location

The task `door-open-wall` requires the robot to pull the door open to the left with a wall in the way.
To pull the door open to the left with a wall in the way reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    If the gripper is not above the door handle, move it above the door handle.
    - When the robot's gripper is not above door handle, move the robot's gripper until the robot's gripper is almost vertically aligned with door handle and the robot's gripper is closed
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is vertically aligned with door handle, move the robot's gripper until the robot's gripper is left of the door handle

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location, but with a wall in the way.
To pick up the puck and hold it at the target location, but with a wall in the way reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  