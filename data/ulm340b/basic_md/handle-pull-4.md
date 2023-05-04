
    - When the robot's gripper is not above handle, the robot should put gripper above handle.
    - When the robot's gripper is not around handle, the robot should put gripper around handle.
    - When the robot's gripper is around handle, the robot should pull handle up.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, what steps the robot should perform?
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle,