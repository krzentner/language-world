

Steps: 
1. Put the gripper above the hammer handle
2. Drop the gripper around the hammer handle
3. Move the gripper down towards the nail
4. Swing the hammer up and hit the nail

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the gripper above the hammer handle
    if check("the robot's gripper is not above the hammer handle"):
        robot.put("gripper above hammer handle")
    #  2. Drop the gripper around the hammer handle
    if check("the robot's gripper is not around the hammer handle and the robot's gripper is open"):
        robot.drop("gripper around hammer handle")
    #  3. Move the gripper down towards the nail
    if check("the robot's gripper is around the hammer handle and the robot's gripper is not near the nail"):
        robot.move("gripper towards nail")
    #  4. Swing the hammer up and hit the nail
    if check("the robot's gripper is near the nail"):
        robot.swing("hammer up to hit nail")
```