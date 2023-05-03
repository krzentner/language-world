To slide the puck backwards to the target location, the robot should perform the following steps:

1. Put the gripper above the puck
   - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
2. Drop the gripper around the puck
   - When the robot's gripper is not around the puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
3. Slide the puck backwards to the goal
   - If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
     - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck, move the robot's gripper until the robot's gripper is above the puck and the robot's gripper is closed
   - If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.
     - When the robot's gripper is near the puck and the puck is below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location and the robot's gripper is open (to release the puck)