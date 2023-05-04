

You may use the function `check(statement)`, which will return whether `statement` is true or false. For example, `check("the robot's gripper is around the puck")` will return `True` or `False` depending on whether the robot's gripper is around the puck.

You may also use the function `robot.put("description")`, which will command the robot to move its gripper to the location described by `description`. The descriptions are: `above`, `below`, `left of`, `right of`, `behind`, `in front of`, and `near`. For example, `robot.put("gripper above the robot's gripper")` will move the gripper above the puck (assuming the robot is currently holding the puck), and `robot.put("the gripper near the robot's gripper")` will move the gripper near the puck.

You may also use `robot.grab("object")`, which moves the robot's gripper around the specified object. It moves the robot's gripper above the object, drops the gripper around the object, and closes the gripper around the object. For example, `robot.grab("puck")` will grab the puck.

You may also use `robot.push("description")`, which will push the object as described by `description`. For example, `robot.push("the puck to the target")` will push the puck so it is at the target.

You may also use `robot.insert("object into container")`, which inserts the object into the container. For example, `robot.insert("peg into the hole")` will insert the peg into the hole.

You may also use `robot.turn("description")`, which will turn the object as described by `description`. For example, `robot.turn("the dial clockwise")` will turn the dial clockwise.

The task is complete when the gripper is around the dial and the dial is turned.

```
def dial_turn(robot):
    if check("the robot's gripper is not above dial"):
        robot.put("the gripper above dial")
    if check("the robot's gripper is not forward aligned with dial"):
        robot.grab("dial")
    if check("the robot's gripper is not around dial"):
        robot.turn("dial clockwise")

## Example run:

>>> start_task('dial-turn')
The robot's gripper is above dial.
The robot's gripper is forward aligned with dial.
The robot's gripper is around dial.
The task is complete.
```
""",
    "task_