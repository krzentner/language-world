The task `basketball` requires the robot to pick up the ball, move it to a position above the hoop, and drop it so that it goes through the hoop. To put the ball into the hoop reliably, the robot should perform the following steps:

Steps:  1. Put gripper above the ball  2. Drop gripper around the ball  3. Close gripper around the ball  4. Move ball above the hoop  5. Open gripper to drop the ball into the hoop

First, move the gripper above the ball.
- When the robot's gripper is not above the ball, move the robot's gripper until the robot's gripper is above the ball
Next, drop the gripper around the ball and close it to grab the ball.
- When the robot's gripper is not around the ball and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the ball and the robot's gripper is closed
Move the ball to a position above the hoop.
- When the robot's gripper is holding the ball and the ball is not above the hoop, move the robot's gripper until the ball is above the hoop
Open the gripper to drop the ball into the hoop.
- When the robot's gripper is holding the ball and the ball is above the hoop, open the gripper to drop the ball into the hoop.