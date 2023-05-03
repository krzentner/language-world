

Steps:
1. Put gripper above the peg
2. Drop gripper around the peg
3. Pull the wrench off the peg

If the robot's gripper is not above the peg, move the gripper to the peg.

```
if check("the robot's gripper is not above the peg"):
    robot.move_gripper("above the peg")
```
    
If the gripper isn't around the peg, drop it around the peg.

```
if check("the robot's gripper is not around the peg"):
    robot.move_gripper("around the peg")
```

If the gripper is around the peg, pull off the wrench by retracting the gripper from the peg.

```
if check("the robot's gripper is around the peg"):
    robot.move_gripper("upwards away from the peg")
```