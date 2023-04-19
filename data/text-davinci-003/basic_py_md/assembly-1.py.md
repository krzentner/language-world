

Your code here:
```
# assembly: put the wrench around the peg
# def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.grab("wrench")
    if check("the progress nut is not left of the robot's gripper and the gripper is not forward aligned with the progress nut"):
        robot.align("gripper with progress nut")
    if check("the progress nut is forward aligned with the robot's gripper and the wrench is not around the peg"):
        robot.put("wrench around the peg")
    if check("the wrench is now around the peg and the progress nut is far from the progress nut"):
        robot.slide("wrench down the peg")
```