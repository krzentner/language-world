

Next, the program should define the steps for the robot to follow.

```
# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Slide soccer ball to goal
    # First, move the gripper above the soccer ball
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the soccer ball is below the gripper, push down with the gripper to
    # trap the soccer ball.
    if check("the robot's gripper is above the soccer ball and the soccer ball is below the robot's gripper"):
        robot.move_gripper("above the soccer ball", close_gripper=True)
    # If the soccer ball is trapped, slide it to the target location.
    if check("the robot's gripper is above the soccer ball and the soccer ball is below the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("above the target location")
```