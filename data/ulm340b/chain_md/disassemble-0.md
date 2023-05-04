
Steps:  1. Put gripper right of the peg  2. Grab the wrench's grip  3. Pull open the drawer
    First, put the gripper right of the peg, so that we can grab the wrench handle from the side.
    - When the robot's gripper is left of the peg, the robot should move to the right of the peg.
    If the robot's gripper is near the peg but not around it, grab the peg handle.
    - When the robot's gripper is near the peg and the robot's gripper is not around the peg, the robot should grab wrench handle.
    If the robot's gripper is around the peg and the robot's gripper is above the peg, pull the wrench off the peg.
    - When the robot's gripper is around the peg and the robot's gripper is above the peg, the robot should pull wrench off peg.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, what steps the robot should perform?
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
Steps:  1. Put gripper left of the window handle  2. Start pushing against the window handle to close the window  3. Push the window closed harder
    If the the window handle is right of the robot's gripper, we should move the gripper near the window handle to start pushing
    - When the window