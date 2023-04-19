To pick up the puck and hold it at the target location, the robot should perform the following steps:
1. Put the gripper roughly above the puck, so that we don't bump it while trying to grab it.
2. When the robot's gripper is not above the puck, the robot should place the gripper above the puck.
3. If the gripper isn't around the puck, put it around the puck.
4. When the robot's gripper is not around the puck and the robot's gripper is open, the robot should drop the gripper around the puck.
5. If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
6. When the robot's gripper is near the puck and the robot's gripper is open, the robot should close the gripper around the puck.
7. We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to move the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
8. When the robot's gripper is above the puck and the robot's gripper is closed, the robot should move the puck to the goal.
9. Once the robot has reached the goal, the gripper should release the puck by opening it.