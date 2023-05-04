
    - When the robot's gripper is not vertically aligned with peg, the robot should put gripper above peg.
    - When the robot's gripper is not left of wrench and the robot's gripper is not horizontally aligned with wrench, the robot should put gripper around wrench.
    - When the robot's gripper is above wrench, the robot should pull away from peg.

The task `button-press-side` requires the robot to push the button with its gripper from the side.
To push the button with its gripper from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is below button, the robot should put gripper right of button.
    - When the robot's gripper is right of button, the robot should put gripper around button.
    - When the robot's gripper is around button, the robot should press button.

The task `pick-place-with-camera` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `pick` requires the robot to pick up the small puck and hold it in its gripper.
To pick up the small puck and hold it in its gripper reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the small puck, the robot should place gripper above small puck.
    - When the robot's gripper is not around small puck and the robot's gripper is open, the robot should drop gripper around small puck.
    - When the robot's gripper is near small puck and the robot's gripper is open, the robot should close gripper around small puck.

The task `pick-orient-place` requires the robot to pick up the puck, orient it vertically and hold it at the target location.
To pick up the puck, orient it vertically and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above