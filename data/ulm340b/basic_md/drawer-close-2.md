

(a)  When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.

(b)  When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should push drawer close.

(c)  When the robot's gripper is around drawer handle, the robot should push drawer handle away from drawer.

> 1, 2, 3. The robot's gripper should be around the drawer handle and vertically aligned with the handle before the robot can push the drawer close. Once the gripper is around and aligned, it can push the drawer close.

The task `handle-press` requires the robot to press down on the handle.
To press down on the handle reliably, what steps the robot should perform?

(a)  When the robot's gripper is not vertically aligned with handle, the robot should put gripper above handle.

(b)  When the robot's gripper is not around handle, the robot should put gripper around handle.

(c)  When the robot's gripper is around handle, the robot should push down on handle.

> 1, 2, 3. The robot's gripper should be around the handle and vertically aligned with the handle before the robot can push down on the handle. Once the gripper is around and aligned, it can push down on the handle.

The task `button-press` requires the robot to push the button to the left.
To push the button to the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button and the robot's gripper is not right of button, the robot should put gripper above button.
    - When the robot's gripper is near button, the robot should slide button left.
    - When the robot's gripper is left of button, the robot should push button left harder.

The task `peg-unplug-side` requires the robot to grab the peg and pull it out of the hole from the side.
To grab the peg and pull it out of the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When the robot's gripper is above the peg and the robot's gripper is not forward aligned with the peg, the robot should put gripper around peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
