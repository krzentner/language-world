The task `basketball` requires the robot to pick up the ball, move it to the hoop, and drop it into the hoop. To put the ball into the hoop reliably, the robot should perform the following steps:

    Steps:  1. Put gripper above the ball  2. Close gripper around the ball  3. Move gripper to above the hoop  4. Drop the ball into the hoop
    First, put the gripper above the ball.
    - When the robot's gripper is not above the ball, move the robot's gripper until the robot's gripper is above the ball
    Then, close the gripper around the ball.
    - When the robot's gripper is above the ball and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the ball and the robot's gripper is closed
    Next, move the gripper to above the hoop.
    - When the robot's gripper is not above the hoop, move the robot's gripper until the robot's gripper is above the hoop
    Finally, drop the ball into the hoop by opening the gripper while the gripper is above the hoop.
    - When the robot's gripper is above the hoop and the robot's gripper is closed, move the robot's gripper until the robot's gripper is above the hoop and the robot's gripper is open