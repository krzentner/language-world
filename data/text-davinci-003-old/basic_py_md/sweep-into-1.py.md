

Solution:
```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    if check("the robot's gripper is not near the cube"):
        robot.reach("to cube") 
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.drop("gripper around cube") 
    if check("the robot's gripper is around the cube"):
        robot.lift("cube")
    if check("the cube is above the robot's gripper"):
        robot.move("cube to goal")
```