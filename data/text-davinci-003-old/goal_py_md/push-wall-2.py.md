

The robot needs to be able to slide the puck to the target location while a wall is in the way. 

Steps:
1. Put gripper above puck
2. Push gripper into top of puck
3. Slide puck to goal

First, the robot needs to put the gripper roughly above the puck, so it doesn't bump it while attempting to grab it. 

```
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")
``` 

If the gripper isn't around the puck, it needs to be moved around the puck. 

```
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)
```

Once the gripper is near the puck and it is closed, the robot needs to move its gripper to the side of the wall. 

```
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move_gripper("near the side of the wall")
```

Once the gripper is near the wall, the robot can move it to the other side of the wall to slide the puck to the target. 

```
if check("the robot's gripper is near the side of the wall"):
    robot.move_gripper("on the other side of the wall")
```

Finally, the robot can move its gripper to the target location to complete the task. 

```
if check("the robot's gripper is on the other side of the wall"):
    robot.move_gripper("near the target location")
```