

Solution:

```
# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is around wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.place("wrench around peg")
```