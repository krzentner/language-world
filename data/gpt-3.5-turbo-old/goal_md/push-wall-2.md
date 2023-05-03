To slide the puck to the target location with a small wall in the way reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to wall  4. Move gripper up and over the wall  5. Slide puck to target
    The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    If the gripper is near the puck, we've probably trapped the puck and can slide it to the wall. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the puck is at the wall and the robot's gripper is closed
    Once the puck is at the wall, we need to move the gripper up and over it.
    - When the robot's gripper is holding the puck against the wall, move the robot's gripper until the robot's gripper is above the wall and the robot's gripper is still holding the puck
    Finally, we can slide the puck to the target location.
    - When the robot's gripper is above the wall and the puck is lined up with the target location, move the robot's gripper until the robot's gripper is above the target location