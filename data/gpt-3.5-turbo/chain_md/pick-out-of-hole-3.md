The task `pick-out-of-hole` may require several attempts to pick up the peg from the hole. The robot should perform the following steps:

    Steps:  1. Put gripper above peg  2. Move gripper down and attempt to grab peg  3. If gripper misses, move gripper back above the peg and try again  4. Close gripper around peg once it is grasped  5. Move the peg to the target location
    
First, put the gripper above the peg in the hole. 

- When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.

Attempt to grab the peg by moving the gripper down to the hole.

- When the robot's gripper is above the hole and the robot's gripper is not closed around the peg, the robot should move gripper down and attempt to grab peg.

If the gripper misses, move the gripper back above the peg and try again.

- When the robot's gripper is not closed around the peg and the peg is not grasped, the robot should move gripper back above the peg and try again.

Once the gripper has grasped the peg, close the gripper around it.

- When the robot's gripper is closed around the peg, the robot should hold onto the peg and move it to the target location. 

Finally, move the peg to the target location.

- When the robot's gripper is above the target location and the peg is held by the gripper, the robot should release the peg at the target location.