

Steps: 
  1. Put gripper horizontally aligned with the peg 
  2. Open gripper around the peg
  3. Slide the peg sideways outside the hole
 
If the gripper is not horizontally aligned with the peg, move the gripper to become horizontally aligned with the peg. 

```
    if check("the robot's gripper is not horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")
``` 

If the gripper is horizontally aligned but not around the peg, open the gripper around the peg. 

```
    if check("the robot's gripper is not around peg and the robot's gripper is closed"):
        robot.move_gripper("around the peg", open_gripper=True)
``` 

If the gripper is near the peg, slide the peg sideways outside the hole. 

```
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("horizontally aligned with hole outside of it")
```