

- When the robot's gripper is not around faucet handle, the robot should move gripper around faucet handle.
- When the robot's gripper is around faucet handle, the robot should turn faucet left.

The task `push-pull` requires the robot to move the puck to the target location.
To move the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should push the puck left.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle and the robot's gripper is right of door handle, the robot should move gripper to left of door handle.
    - When the robot's gripper is almost vertically aligned with the door handle, the robot should push door closed.

The task `peg-unplug` requires the robot to pull the peg out of the hole and return it to the original location.
To pull the peg out of the hole and return it to the original location reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    - When the robot's gripper is near peg, the robot should grab peg.
    - When peg is forward aligned with the robot's gripper, the robot should move gripper to the left of the peg.
    - When the robot's gripper is left of peg, the robot should move gripper to the right of peg.
    - When the robot's gripper is right of peg, the robot should let go of peg.

The task `faucet-close` requires the robot to turn the faucet right.
To turn the faucet right reliably, the robot should perform the following steps:
    - When the robot's gripper is not around faucet handle, the robot should move gripper around faucet handle.
    - When the robot's gripper is around faucet handle, the robot should turn faucet right.

The task `slide-back` requires the robot to slide the puck back to the original location.
To slide the puck back to the original location reliably,