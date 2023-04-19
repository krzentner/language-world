

Here's the code to perform the assembly task:

```
# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.grab("wrench")
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.align("wrench around peg")
    if check("the robot's gripper is aligned with the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
```