Here's the program to perform the `pick-out-of-hole` task:

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    if check("the robot's gripper is not near the hole"):
        robot.move("to the hole")
    if check("the robot's gripper is not around the peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is not closed around the peg"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above the hole and the peg is in the gripper"):
        robot.move("to the goal")
``` 

This code instructs the robot to move to the hole, grab the peg, and move to the goal while holding onto the peg.