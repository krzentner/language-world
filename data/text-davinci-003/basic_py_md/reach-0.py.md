

Keep in mind that the `check()` function will return `True` if the given condition has been met.

```
# reach: reach to the target location
def reach(robot):
    if check("the robot is not near the target location"):
        robot.move("to the target location")
    if check("the robot is near the target location"):
        robot.stop("at the target location")
    if check("the robot is not facing the target location"):
        robot.turn("to face the target location")