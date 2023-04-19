```
# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    if check("the robot's gripper is not holding the stick and the stick is not touching the thermos"):
        robot.grab("the stick")
    if check("the stick is touching the thermos and the robot's gripper is not holding the thermos"):
        robot.align("the stick with the thermos")
    if check("the stick is aligned with the thermos and the robot's gripper is not holding the thermos"):
        robot.pull("the thermos towards the goal with the stick")
    if check("the thermos is at the goal location"):
        robot.drop("the thermos")    
```