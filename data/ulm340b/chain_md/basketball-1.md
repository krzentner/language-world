

    - When the ball is not above the gripper, the robot should grab the ball.
    - When the ball is above the gripper and the gripper is not open, the robot should let go of the ball.
    - When the ball is above the gripper and the ball is not near the hoop, the robot should move the ball towards the hoop.

The task `pick-place-back` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it. Try to move the puck to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck at goal.

The task `sweeping` requires the robot to clean up the dust into the dustpan.
To clean up the dust into the dustpan reliably, what steps the robot should perform?

    - When dustpan isn't aligned with the broom, the robot should align the broom with the dustpan.
    - When dustpan isn't behind the broom and the broom isn't below the dustpan, the robot should put the broom behind the dustpan.
    - When dustpan is aligned with the broom and the broom is behind the dustpan, the robot should sweep dust into dustpan.

The task `peg-unplug-side` requires the robot to grab the peg and pull it out from the side.
To grab the peg and pull it out from the side reliably, what steps the robot should perform?

    - When