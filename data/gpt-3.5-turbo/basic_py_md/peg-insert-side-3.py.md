Here's the program to perform the `peg-insert-side` task using the robot:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not near the peg"):
        robot.reach("the peg")
        robot.put("the gripper above the peg")
        robot.grab("the peg")
        robot.put("the gripper above the hole")
        robot.move("the gripper to the side of the hole")
        robot.push("the peg into the hole")
        robot.release()
```

In this program, the robot first uses the `reach()` method to move the gripper close to the peg and then `put()` the gripper above it. Then, it uses `grab()` to hold onto the peg and moves the gripper above the hole using `put()`. Next, it moves the gripper to the side of the hole using `move()` and pushes the peg into the hole using `push()`. Finally, the robot releases the peg using `release()`.