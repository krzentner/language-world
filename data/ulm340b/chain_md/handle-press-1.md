We can try different strategies and see what works:
    - When the robot's gripper is not vertically aligned with handle and the robot's gripper is below the handle, the robot should put the gripper above the handle.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle, the robot should put the gripper near the handle.
    - When the robot's gripper is near handle, the robot should push handle down.

The task `switch-press` requires the robot to push the switch all the way up.
To push the switch all the way up reliably, what steps the robot should perform? We can try different strategies and see what works:
    - When the robot's gripper is not vertically aligned with switch and the robot's gripper is above the switch, the robot should put the gripper below the switch.
    - When the robot's gripper is vertically aligned with switch and the robot's gripper is not near switch, the robot should put the gripper near the switch.
    - When the robot's gripper is near switch, the robot should push switch up.

The task `button-press-side` requires the robot to push the button in from the side.
To push the button in from the side reliably, what steps the robot should perform? We can try different strategies and see what works:
    - When the robot's gripper is not forward aligned with button and the robot's gripper is right of the button, the robot should put the gripper left of the button.
    - When the robot's gripper is forward aligned with button and the robot's gripper is not near button, the robot should put the gripper near the button.
    - When the robot's gripper is near button, the robot should push button in.

The task `pick-out-of-hole` requires the robot to pick the peg out of the hole.
To pick the peg out of the hole reliably, what steps the robot should perform? We can try different strategies and see what works:
    - When the robot's gripper is not vertically aligned with peg and the robot's gripper is below the peg, the robot should put the gripper above the peg.
    - When the robot's gripper is vertically aligned with peg and the robot's gripper is not near peg, the robot should put the gripper near the peg.
    - When the robot's gripper is near peg, the robot should grab the peg.
    - When the robot's gripper is grabbing peg, the robot should move gripper up.

The task `toggle-switch-off` requires the robot to flip the switch down.
