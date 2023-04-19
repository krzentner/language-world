

Steps: 
1. Put gripper above the wrench
2. Drop gripper around the wrench
3. Pull wrench off the peg

If the robot's gripper is not above the wrench, we should move it there.
```
if check("the robot's gripper is not above the wrench"):
    robot.move_gripper("above the wrench")
```

If the gripper isn't around the wrench, put it around the wrench.
```
if check("the robot's gripper is not around wrench and the robot's gripper is open"):
    robot.move_gripper("near the wrench", close_gripper=True)
```

Once the gripper is around the wrench, pull the wrench off the peg.
```
if check("the robot's gripper is around wrench"):
    robot.move_gripper("above the peg")
```