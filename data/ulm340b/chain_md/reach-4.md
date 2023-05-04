
    Steps:  1. Get robot's gripper near goal
    Get the gripper close to the target.
    - When the robot's gripper is not near goal, the robot should move gripper to goal.

The task `push-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above button  2. Push down on button from top
    If the robot's gripper is not vertically aligned with button, put gripper above button.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    If the robot's gripper is vertically aligned with button, push down on button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `peg-insert-topdown` requires the robot to put the peg into the hole from above.
To put the peg into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Put the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg is not to the left of the gripper, grab it.
    - When the peg is not left of the robot's gripper, the robot should grab peg.
    Now that the peg is in the gripper, just line up the peg with the hole as seen from above and drop it.
    - When the peg is forward aligned with the robot's gripper, the robot should put peg into hole.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Push door handle closed
    First, put the gripper roughly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    Now just push it closed.
    - When the robot's gripper is almost vertically aligned with door handle, the robot should push door handle closed.

The task `button-press-side` requires the robot to push the button to the side.
To push the button to the side reliably, the robot should