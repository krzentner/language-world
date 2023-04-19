

This program should allow the robot to pick-up a basketball and shoot it into a basketball hoop. 

Steps:
1. Line up the gripper with the ball
2. Grab the ball with the gripper
3. Move the ball to the hoop
4. Line up the ball with the hoop and shoot

```
# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Line up the gripper with the ball
    #  2. Grab the ball with the gripper
    #  3. Move the ball to the hoop
    #  4. Line up the ball with the hoop and shoot
    # First, line up the gripper with the ball.
    if check("the robot's gripper is not forward aligned with the ball"):
        robot.put("gripper aligned with ball")
    # If the gripper is aligned with the ball, we should be able to grab the
    # ball.
    if check("the robot's gripper is forward aligned with the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # If the gripper is around the ball with the ball close, we can start
    # moving the ball to the hoop.
    if check("the robot's gripper is around ball and the ball is close to the gripper"):
        robot.move("ball to the hoop")
    # Once the ball is near the hoop, line it up with the hoop and shoot.
    if check("the ball is near the hoop but not aligned"):
        robot.align("ball to the hoop")
    # Shoot the ball.
    if check("the ball is aligned with the hoop"):
        robot.release("gripper from ball")
```