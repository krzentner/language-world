

Then complete the function: 

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop gripper around the ball
    #  3. Align the ball with the hoop
    #  4. Push the ball towards the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball", close_gripper=True)
    # If the ball goes below the gripper, go back to putting the gripper above
    # the ball.
    if check("the robot's gripper is open and the ball is not above the robot's gripper"):
        robot.move_gripper("above the ball")
    # If the ball is locked in the gripper, align the ball with the hoop by
    # moving the gripper left or right.
    if check("the ball is above the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("left of the hoop")
    # If the ball is lined up with the hoop, then just push the ball at the
    # hoop.
    if check("the ball is in front of the hoop"):
        robot.move_gripper("near the hoop")
```