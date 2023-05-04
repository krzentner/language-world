

The task `soccer-notarget` requires the robot to move the soccer ball out of the way.
To move the soccer ball out of the way reliably, what steps the robot should perform?

The task `pick-place-side` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the puck  2. Grab the puck with the gripper  3. Slide the puck sideways to the goal
    First, put the gripper above the puck.
    - When the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    If the puck is below the gripper, close the gripper.
    - When the puck is below the robot's gripper and the robot's gripper is open, move the robot's gripper until the robot's gripper is closed
    If we have the gripper around the puck, we can slide the puck to the target location.
    - When the robot's gripper is around the puck, move the robot's gripper until the robot's gripper is near the target location

The task `peg-unstack` requires the robot to pull the top peg out of the hole.
To pull the top peg out of the hole reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper around the top peg  2. Pull up on the top peg
    Put the gripper around the top peg so you can pull it out.
    - When the robot's gripper is not around the top peg and the robot's gripper is not below the top peg, move the robot's gripper until the robot's gripper is around the top peg
    If you can get the gripper below the top peg, then pull the peg out by pulling up on the top peg.
    - When the robot's gripper is around the top peg and the robot's gripper is not below the top peg, move the robot's gripper until the robot's gripper is below the top peg

The task `ball-in-cup-insert` requires the robot to insert the ball into the cup by grabbing the ball.
To insert the ball into the cup by grabbing the ball reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above ball  2. Grab the ball with the gripper  3. Drop ball into the cup
    If the ball