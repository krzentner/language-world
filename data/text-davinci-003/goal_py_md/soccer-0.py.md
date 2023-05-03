

Steps: 
1. Place the robot's gripper above the soccer ball
2. Push down to trap the soccer ball 
3. Move the robot's gripper to the target location

```
# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Place the robot's gripper above the soccer ball
    #  2. Push down to trap the soccer ball 
    #  3. Move the robot's gripper to the target location
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # Once the gripper is above the soccer ball, trap it by pushing the gripper
    # down onto the ball.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not trapping the soccer ball"):
        robot.move_gripper("trapping the soccer ball")
    # Once the soccer ball is trapped, move the gripper to the target location.
    if check("the robot's gripper is trapping the soccer ball"):
        robot.move_gripper("above the target location")
```