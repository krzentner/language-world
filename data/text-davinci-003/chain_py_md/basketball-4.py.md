

```
# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop gripper around the ball
    #  3. Lift ball
    #  4. Move ball towards the hoop
    #  5. Move closer to the basket
    #  6. Drop ball
    # First, put the gripper above the ball to not have a direct contact.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # If the gripper is not around the ball, let's put the gripper around it
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # Once we got the gripper around the ball, let's lift the ball up
    if check("the robot's gripper is around the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # Now we can move the ball towards the hoop.
    if check("the robot's gripper is around the ball and the robot's gripper is closed"):
        robot.move("ball towards hoop")
    # Once we are close to the hoop, let's move closer to the basket.
    if check("the robot is close to the hoop"):
        robot.move("closer to basket")
    # Now that we are close enough to the basket, we can drop the ball.
    if check("the robot is close to the basket"):
        robot.release("ball into hoop")
```