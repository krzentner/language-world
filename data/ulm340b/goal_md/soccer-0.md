
    Steps:  1. Put the gripper near the ball  2. Push the ball to the goal
    The robot can push the soccer ball by moving into it. If the ball isn't near the gripper, move the gripper to the ball.
    - When the robot's gripper is not near the soccer ball, move the robot's gripper until the robot's gripper is near the soccer ball
    If the robot's gripper is near the ball, we can try to push the ball to the goal.
    - When the robot's gripper is near the soccer ball, move the robot's gripper until the robot's gripper is near the target location

The task `pick-place-with-clutter` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the puck, move the robot's gripper until the robot's gripper is above the puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above puck and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location

The task `button-press` requires the robot to push the button down.
To push the button down reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is not "topdown", we need to be careful to line the gripper up on all sides. Line up the robot's gripper from above.
    - When the robot's gripper is not aligned with button, move the robot's gripper until the robot's gripper is aligned with the button
    Now that the gripper is lined up,