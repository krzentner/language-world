

```
# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not near the wrench"):
        robot.move("gripper above wrench")
    if check("the robot's gripper is far from the peg"):
        robot.move("gripper near peg")
    if check("the robot's gripper is not above the peg and the robot's gripper is not around the peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around the peg and the wrench is not open"):
        robot.open("wrench")
    if check("the robot's gripper is near the wrench and the wrench is open"):
        robot.drop("wrench around peg")
    if check("the robot's gripper is around the peg and the wrench is closed"):
        robot.lift("wrench away from peg")
```