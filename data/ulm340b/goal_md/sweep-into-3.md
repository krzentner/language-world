(The robot can probably grab the cube by moving the gripper down around the cube.)

The task `pick-place-side` requires the robot to grab the puck and hold it against the target location.
To grab the puck and hold it against the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move gripper against goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above puck and the robot's gripper is closed, move the robot's gripper until the robot's gripper is vertically aligned with the target location

The task `button-press-side` requires the robot to push the button with the gripper, to the side.
To push the button with the gripper, to the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above button  2. Drop gripper around button  3. Press button
    First, put the gripper above button, so that it doesn't get pushed while we are moving the gripper around it.
    - When the robot's gripper is not above the button, move the robot's gripper until the robot's gripper is above the button
    If the gripper isn't around the button, move it around the button.
    - When the robot's gripper is not around button, move the robot's gripper until the robot's gripper is around the button
    If the gripper is around the button, press the button.
    - When the robot's gripper is above button, move the robot's gripper until the robot's gripper is near the button

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    