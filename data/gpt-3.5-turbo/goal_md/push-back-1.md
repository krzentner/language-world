To slide the puck backwards to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Push gripper down on top of puck  3. Slide puck backwards towards goal
    The robot can slide the puck backwards by trapping it by pushing down on it from above and moving the gripper in the opposite direction. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    - When the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it backwards.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
    If the gripper is near the puck, we've probably trapped the puck and can slide it backwards towards the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper backwards until the robot's gripper is above the target location