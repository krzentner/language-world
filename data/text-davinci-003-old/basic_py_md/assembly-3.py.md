

Here's the code to perform the 'assembly' task:

```
# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.reach("to wrench")
    if check("the robot's gripper is not around the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is not above the peg"):
        robot.reach("to peg")
    if check("the robot's gripper is not around the peg and the robot's gripper is not open"):
        robot.open("gripper around peg")
    if check("the robot's gripper is around the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
```