

The goal of this task is to turn the dial in a clockwise direction. 

Steps:

1. Put gripper above the dial 
2. Drop the gripper around the dial
3. Turn the dial clockwise

First, put the gripper above the dial, so that we don't bump it when trying to grab it.

```
if check("the robot's gripper is not above the dial"):
    robot.put("gripper above dial")
```

Once the gripper is lined up above the dial, we should be able to grab the dial by moving the gripper down around it. 

```
if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not around dial"):
    robot.drop("gripper around dial")
```

Once the gripper is around the dial, we can just turn the dial clockwise. 

```
if check("the robot's gripper is around dial"):
    robot.rotate("clockwise")
```