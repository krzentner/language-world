
Steps:  1. Put gripper above puck  2. Push gripper into top of puck  3. Slide puck to goal
The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper. If the puck isn't below the gripper as seen from above, move the gripper above the puck.
If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. Close the gripper to make sure we keep control of the puck.

The task `reach-pick-place-back` requires the robot to reach back to the target location.
To reach back to the target location reliably, the robot should perform the following steps:
Steps:  1. Reach towards the target
We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
If the robot's gripper is not near reach target, the robot should reach to goal.

The task `reach-pick-place-side` requires the robot to reach to the side to the target location.
To reach to the side to the target location reliably, the robot should perform the following steps:
Steps:  1. Reach towards the target
We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
If the robot's gripper is not near reach target, the robot should reach to goal.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
Steps:  1. Put gripper above the button  2. Push down on the button from the side
Because this is "side", we just need to put the gripper above the button and push down on it.
If the robot's gripper is not above button, the robot should put the gripper above button.
Now that the gripper is lined up, just push down on the button.
If the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `button-press-angled` requires the robot to push the button from an angle.
To push the button from an angle reliably, the robot should perform the following steps:
Steps:  1. Put gripper above the button  2. Push down on the button
Because this is "angled", we just need to put the gripper above the button and push down on it.
If the robot's gripper is not above button,