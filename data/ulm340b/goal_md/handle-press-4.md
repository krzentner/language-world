
    Steps:  1. Put gripper above the handle  2. Push the handle down from the top
    The robot can push down the handle by trapping it by pushing down on it from above and moving the gripper. If the handle isn't below the gripper as seen from above, move the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, move the robot's gripper until the robot's gripper is vertically aligned with the handle
    If the gripper is aligned with the handle but not near it, move the gripper down to the handle to push it.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle, move the robot's gripper until the robot's gripper is near the handle

The task `knob-turn-cw-topdown` requires the robot to rotate the knob clockwise as seen from above.
To rotate the knob clockwise as seen from above reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the knob  2. Turn the knob from above clockwise
    The robot can rotate the knob by grabbing it by putting the gripper around the knob. If the knob isn't below the gripper as seen from above, move the gripper above the knob.
    - When the robot's gripper is not vertically aligned with knob, move the robot's gripper until the robot's gripper is vertically aligned with the knob
    If the gripper is aligned with the knob but not near it, move the gripper down around the knob to turn it.
    - When the robot's gripper is vertically aligned with knob and the robot's gripper is not around knob, move the robot's gripper until the robot's gripper is around the knob

The task `drawer-side` requires the robot to pull the drawer open.
To pull the drawer open reliably, what steps the robot should perform?
    Steps:  1. Put gripper below the drawer handle  2. Raise gripper around the drawer handle  3. Pull open the drawer
    We need to put the gripper below the drawer handle before we can grab it, because of the angle of the robot's gripper.
    - When the robot's gripper is not horizontally aligned with drawer handle, move the robot's gripper until the robot's gripper is horizontally aligned with the drawer handle
    Once the gripper is lined up below the drawer handle, we should be able to grab the drawer handle by moving the gripper up around it.
    - When the robot's gripper is horizontally aligned