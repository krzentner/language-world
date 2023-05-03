

The program should accomplish the following steps:

1. Put gripper above the ball 
2. Drop gripper around the ball
3. Close grips around the ball
4. Move ball towards the hoop
5. Release the ball when it's close to the hoop

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop gripper around the ball
    #  3. Close gripper around the ball
    #  4. Move ball towards the hoop
    #  5. Release the ball when it's close to the hoop
    # First, put the gripper roughly above the ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # As long as the gripper is near the ball and closed, move the ball to the hoop.
    if check("the robot's gripper is near the ball and the robot's gripper is closed"):
        robot.move_gripper("near the hoop")
    # When the ball is close to the hoop, release the gripper.
    if check("the ball is close to the hoop"):
        robot.open_gripper()