
    - If the target location is not above the robot's gripper and the target location is not in front of the robot's gripper and the target location is not left of the robot's gripper, move the robot's gripper until the target location is above the robot's gripper
    - If the target location is not above the robot's gripper, move the robot's gripper until the target location is above the robot's gripper

The task `pick-place-side` requires the robot to pick up the peg and hold it at the target location.
To pick up the peg and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper around the peg  2. Close gripper around the peg  3. Move the peg to the target location
    Step 1. First, put the gripper around the peg.
    - When the robot's gripper is not around peg, move the robot's gripper until the robot's gripper is around peg and the robot's gripper is closed
    Step 2. If the robot's gripper is around the peg, close the gripper around the peg.
    - When the robot's gripper is not closed, move the robot's gripper until the robot's gripper is closed
    Step 3. If the robot's gripper is around the peg and the robot's gripper is closed, move the peg to the target location.
    - When the robot's gripper is around peg and the robot's gripper is closed, move the robot's gripper until the robot's gripper is above the target location and the robot's gripper is closed

The task `button-press-side` requires the robot to push the button.
To push the button reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push the button
    If the button is not left of the gripper and not aligned with it, we should move the gripper so that it's lined up to the side of the button.
    - When button is not left of the robot's gripper and button is not forward aligned with the robot's gripper, move the robot's gripper until the button is forward aligned with the robot's gripper
    Once the gripper is around the button, the robot should just push it.
    - When button is not left of the robot's gripper, move the robot's gripper until the robot's gripper is left of button

The task `plug` requires the robot to put the