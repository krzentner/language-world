Here's the code to perform the `door-open` task:

```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not near the doorknob"):
        robot.move("gripper to the left of the doorknob")
    if check("the robot's gripper is left of the doorknob"):
        robot.grab("doorknob")
    if check("the robot's gripper is around the doorknob"):
        robot.pull("the gripper towards the robot to open the door")
``` 

This code assumes that the robot is facing the door and the doorknob is on the left side of the door. If the doorknob is on the right side, change the direction of the movement in the first `if` statement from left to right.