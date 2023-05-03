The robot should perform the following steps to pick up the puck and hold it at the target location reliably:

1. Put the gripper roughly above the puck, so that we don't bump it while trying to grab it.
2. If the robot's gripper is not above the puck, the robot should place gripper above the puck.
3. If the gripper isn't around the puck, the robot puts it around the puck.
4. If the robot's gripper is not around the puck and the robot's gripper is open, the robot should drop gripper around the puck.
5. If the gripper is near the puck and the robot's gripper is open, the robot should close the gripper around the puck.
6. When the robot's gripper is above the puck and the robot's gripper is closed, the robot should move the puck to the goal.

Note that this is a combination of the steps for `reach` and `pick-place`, as we need to first move the gripper to the puck and grab it before moving it to the goal.