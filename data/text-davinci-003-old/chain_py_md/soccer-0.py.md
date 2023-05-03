

Steps:
1. Align the gripper vertically above the soccer ball.
2. Push the gripper into the top of the soccer ball.
3. Slide the soccer ball in the direction of the target location.
4. Push the soccer ball lightly with the gripper as necessary to adjust the direction.

```
# soccer: push the soccer ball into the target location
# def soccer(robot): 
    # Steps:
    #  1. Align the gripper vertically above the soccer ball.
    if check("the robot's gripper is not vertically aligned with the soccer ball"):
        robot.put("gripper above the soccer ball")
    #  2. Push the gripper into the top of the soccer ball.
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.push("the gripper into the top of the soccer ball")
    #  3. Slide the soccer ball in the direction of the target location.
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.slide("the soccer ball to the target location")
    #  4. Push the soccer ball lightly with the gripper as necessary to adjust
    # the direction.
    if check("the tennis ball is slightly incorrectly aligned with the target location"):
        robot.push("the soccer ball lightly with the gripper to adjust the direction")
```