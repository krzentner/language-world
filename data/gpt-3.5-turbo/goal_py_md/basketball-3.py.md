```
# basketball: put the ball into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the gripper to aim at the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper roughly above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper is above the ball, grab the ball with the gripper.
    if check("the robot's gripper is above the ball and the robot's gripper is not around the ball"):
        robot.move_gripper("around the ball", close_gripper=True)
    # Move the gripper to aim at the hoop by aligning the gripper with the hoop.
    if check("the robot's gripper is around the ball"):
        robot.move_gripper("right of the hoop")
    # Once the gripper is aligned with the hoop, open the gripper to drop the ball.
    if check("the robot's gripper is almost vertically aligned with the hoop"):
        robot.move_gripper("above the hoop", close_gripper=False)
```