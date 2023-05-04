
    -

The task `peg-unstack` requires the robot to grab the green peg and move it to the target location.
To grab the green peg and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with green peg, the robot should put gripper above green peg.
    - When the robot's gripper is vertically aligned with green peg and the robot's gripper is not near green peg, the robot should grab green peg.
    - When the robot's gripper is vertically aligned with green peg and the green peg is left of robot's gripper, the robot should move green peg.

The task `drawer-close` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not forward aligned with drawer handle and the robot's gripper is not near drawer handle, the robot should place gripper above drawer handle.
    - When the robot's gripper is near drawer handle and the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper around drawer handle.
    - When the robot's gripper is forward aligned with drawer handle and the robot's gripper is vertically aligned with drawer handle, the robot should push drawer closed.

The task `button-press-side` requires the robot to press the button down from the left.
To press the button down from the left reliably, the robot should perform the following steps:
    - When the robot's gripper is not near button, the robot should put gripper above button.
    - When the robot's gripper is near button and the robot's gripper is not vertically aligned with button, the robot should move robot's gripper right of button.
    - When the robot's gripper is forward aligned with button, the robot should push button in.

The task `button-press-topdown` requires the robot to press the button down from above.
To press the button down from above reliably, what steps the robot should perform?
    -

The task `faucet-close` requires the robot to turn the faucet right.
To turn the faucet right reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the faucet, the robot should put gripper above faucet.
    - When the robot's gripper is near faucet and the robot's gripper is vertically aligned with the faucet, the robot should put gripper around faucet.
    - When the robot's gripper is around faucet and the faucet is not at goal position, the robot should turn faucet right