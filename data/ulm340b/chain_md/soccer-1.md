
    Steps:  1. Put gripper above the ball  2. Put gripper near the ball  3. Push the ball into the target
    First, put the gripper above the ball.
    - When the robot's gripper is not vertically aligned with the ball, the robot should put the gripper above the ball.
    Then put the gripper near the ball.
    - When the robot's gripper is above the ball, the robot should put the gripper near the ball.
    Once the gripper is above the ball, push it to the target.
    - When the robot's gripper is near the ball, the robot should push the ball into the target.

The task `button-press-side` requires the robot to push the button with the gripper.
To push the button with the gripper reliably, the robot should perform the following steps:
    Steps:  1. Put gripper near the button  2. Push the button with the gripper
    If the gripper is not near the button, move it to the button to push it.
    - When the robot's gripper is not near the button, the robot should put the gripper near the button.
    Once the gripper is near the button, push it with the gripper.
    - When the robot's gripper is near the button, the robot should push the button with the gripper.

The task `drawer-open-side` requires the robot to push the drawer open to the side.
To push the drawer open to the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer open
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer open.

The task `peg-unstack` requires the robot to grab the top peg and move it to the target location.
To grab the top peg and move it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Drop gripper around peg  3. Close gripper around peg  4