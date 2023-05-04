

The task `soccer` requires the robot to push the soccer ball into the target location.
To push the soccer ball into the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above soccer ball  2. Push gripper into soccer ball from above  3. Push soccer ball into goal
    The robot can slide the soccer ball by trapping it by pushing down on it from above and moving the gripper. If the soccer ball isn't below the gripper as seen from above, move the gripper above the soccer ball.
    - When the robot's gripper is not vertically aligned with the soccer ball, the robot should place gripper above soccer ball.
    If the gripper is aligned with the soccer ball but not near it, move the gripper down to the soccer ball to slide it.
    - When the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near soccer ball, the robot should push gripper into soccer ball from above.
    If the gripper is near the soccer ball, we've probably trapped the soccer ball and can slide it to the target location.
    - When the robot's gripper is near soccer ball, the robot should push soccer ball to goal.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Push against the side of the button  2. Push the button harder
    Because the button is a very small object, the gripper should align with it from the side. Once aligned with the button, the robot should push on it.
    - When the robot's gripper is not forward aligned with button, the robot should put gripper by button.
    As long as the robot's gripper is forward aligned with the button, we should be able to push it down.
    - When the robot's gripper is forward aligned with button, the robot should push button to the side.

The task `soccer-dribble` requires the robot to push the soccer ball around an obstacle.
To push the soccer ball around an obstacle reliably, what steps the robot should perform?

The task `soccer-dribble` requires the robot to push the soccer ball around an obstacle.
To push the soccer ball around an obstacle reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above soccer ball  2. Push gripper into soccer ball from above  3. Push soccer ball around obstacle
    The robot can slide the soccer ball by trapping it by pushing down on it