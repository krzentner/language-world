
    - When the robot's gripper is not around faucet and the robot's gripper is not above faucet, the robot should put gripper around faucet.
    - When the robot's gripper is vertically aligned with faucet, the robot should rotate faucet to right.

The task `faucet-open` requires the robot to turn the faucet left.
To turn the faucet left reliably, what steps the robot should perform?
    - When the robot's gripper is not around faucet and the robot's gripper is not above faucet, the robot should put gripper around faucet.
    - When the robot's gripper is vertically aligned with faucet, the robot should rotate faucet to left.

The task `sweep` requires the robot to sweep the puck to the target location.
To sweep the puck to the target location reliably, what steps the robot should perform?
    - When the robot's gripper is not above puck and the robot's gripper is not right of puck, the robot should put the gripper above the puck.
    - When the robot's gripper is right of the puck and the robot's gripper is above the puck, the robot should push the gripper right of the puck.
    - When the robot's gripper is right of the puck, the robot should slide puck to goal.

The task `pick-place-wall` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should put gripper above puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should put gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not left of button, the robot should put gripper left of button.
    - When the robot's gripper is not above button, the robot should align gripper to button.
    - When the robot's gripper is above button, the robot should push button.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle