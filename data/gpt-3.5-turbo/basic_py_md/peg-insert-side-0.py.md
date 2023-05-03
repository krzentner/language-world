Here's a program to perform the `peg-insert-side` task:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not near the peg"):
        robot.reach("to the peg")
    if check("the robot's gripper is not around the peg"):
        robot.grab("the peg")
    if check("the robot's gripper is near the hole and the gripper is holding the peg"):
        robot.move("the gripper to the side of the hole")
    if check("the robot's gripper is at the side of the hole and the gripper is holding the peg"):
        robot.put("the peg into the hole")
```

Let me know if you need any assistance with this or anything else.