
    Steps:  1. Place the gripper above the button  2. Push the button down
    You'll need to move the gripper above the button, so we can push it down from above.
    - When the robot's gripper is not above button, the robot should place gripper above button.
    If the robot's gripper is above the button, the robot should push button down.
    - When the robot's gripper is above button, the robot should push button down.

The task `pick-place` requires the robot to pick up the peg and hold it at the target location.
To pick up the peg and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Drop gripper around peg  3. Close gripper around peg  4. Move peg to goal
    First, put the gripper roughly above peg, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the peg, the robot should place gripper above peg.
    If the gripper isn't around the peg, put it around the peg.
    - When the robot's gripper is not around peg and the robot's gripper is open, the robot should drop gripper around peg.
    If the gripper is near the peg and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near peg and the robot's gripper is open, the robot should close gripper around peg.
    We closed the gripper, and the peg is still near the gripper, so maybe we grabbed it. Try to move the peg to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above peg and the robot's gripper is closed, the robot should place peg at goal.

The task `pick-place` requires the robot to pick up the pen and hold it at the target location.
To pick up the pen and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the pen  2. Drop gripper around pen  3. Close gripper around pen  4. Move pen to goal
    First, put the gripper roughly above pen, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the pen, the robot should place gripper above pen.
   