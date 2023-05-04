

    - When the robot's gripper is not on faucet handle, the robot should put gripper on faucet handle.
    - When the robot's gripper is on faucet handle, the robot should rotate faucet handle left.

The task `pick-place-side` requires the robot to pick up the object and hold it at the target location.
To pick up the object and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the object, the robot should place gripper above object.
    - When the robot's gripper is not around object and the robot's gripper is open, the robot should drop gripper around object.
    - When the robot's gripper is near object and the robot's gripper is open, the robot should close gripper around object.
    - When the robot's gripper is above object and the robot's gripper is closed, the robot should place object at goal.

The task `button-press-side` requires the robot to push the button.
To push the button reliably, the robot should perform the following steps:
    - When the robot's gripper is not forward aligned with button and the robot's gripper is not near button, the robot should move gripper to right of button.
    - When the robot's gripper is near button, the robot should push button.

The task `pick` requires the robot to pick up the object.
To pick up the object reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the object, the robot should place gripper above object.
    - When the robot's gripper is not around object and the robot's gripper is open, the robot should drop gripper around object.
    - When the robot's gripper is near object and the robot's gripper is open, the robot should close gripper around object.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    - When the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper, the robot should grab the peg.
    - When the peg is forward aligned with the robot's gripper, the robot should push peg into hole.

The task `door-close` requires the robot to push the door closed.
To push the