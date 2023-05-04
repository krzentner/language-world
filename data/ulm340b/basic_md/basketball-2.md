
    - When the robot's gripper is not above the ball, the robot should reach to ball.
    - When the ball is not near the robot's gripper, the robot should drop gripper around ball.
    - When the robot's gripper is near the ball, the robot should close gripper around ball.
    - When the ball is held by the robot's gripper, the robot should lift ball up.
    - When the robot's gripper is above the ball and the robot's gripper is not above the goal, the robot should reach to goal.
    - When the robot's gripper is above the goal, the robot should release gripper above goal.

The task `button-press-side` requires the robot to push the button from the left side.
To push the button from the left side reliably, the robot should perform the following steps:
    - When the button is not left of the robot's gripper, the robot should put the gripper to the left of the button.
    - When the button is left of the robot's gripper, the robot should push the button.

The task `coffee-button` requires the robot to put the cup below the nozzle and push the button.
To put the cup below the nozzle and push the button reliably, the robot should perform the following steps:
    - When the cup is right of the robot's gripper, the robot should put the gripper above the cup.
    - When the cup is left of the robot's gripper and the cup is not below the nozzle, the robot should pick up the cup.
    - When the cup is below the nozzle, the robot should put down the cup.
    - When the button is left of the robot's gripper, the robot should push the button.
    
The task `soccer` requires the robot to kick the ball towards the goal.
To kick the ball towards the goal reliably, what steps the robot should perform?
    - When the robot's gripper is not above the ball, the robot should reach to ball.
    - When the ball is not near the robot's gripper, the robot should drop gripper around ball.
    - When the robot's gripper is near the ball, the robot should close gripper around ball.
    - When the ball is held by the robot's gripper, the robot should lift ball up.
    - When the robot's gripper is above the ball and the robot's gripper is not above the goal, the robot should reach to goal.
    - When the robot's gripper is above the goal, the robot should release gripper above goal.
'''

class Robot:
    '''A wrapper for Gym environment