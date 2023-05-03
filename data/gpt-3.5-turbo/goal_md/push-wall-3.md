To slide the puck to the target location with a small wall in the way reliably, the robot should perform the following steps:

   Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Move gripper over the wall  4. Align gripper with the new target location  5. Slide puck to goal   
   
The first two steps are the same as for the `push` task (put the gripper above the puck and push the gripper down onto the puck).
   
If there is a wall in the way, the robot needs to move the gripper over the wall so that it can reach the target location on the other side. 
   - When the wall is blocking the robot's gripper, move the robot's gripper to a position where it can fit over the wall 
   
Once the gripper is over the wall, the robot should align the gripper with the new target location.
   - When the robot's gripper is over the wall and not aligned with the new target location, move the gripper to align with the new target location
   
Finally, slide the puck to the goal by moving the gripper while maintaining downward pressure on the puck.
   - While maintaining downward pressure on the puck and the gripper is aligned with the new target location, move the gripper towards the target location to slide the puck to the goal.