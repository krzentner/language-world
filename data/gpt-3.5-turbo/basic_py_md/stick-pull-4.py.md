Here's the program to perform the `stick-pull` task:

```
# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    if check("the robot's gripper is not near the stick"):
        robot.reach("to the stick")
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around the stick")
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.close("gripper around the stick")
    if check("the robot is not near the thermos"):
        robot.move("to the thermos")
    if check("the robot's gripper is not near the thermos and the stick is not between the robot's gripper and the thermos"):
        robot.move("gripper to right of stick")
    if check("the robot's gripper is near the thermos and the stick is between the robot's gripper and the thermos"):
        robot.slide("thermos to the goal")
``` 

This program follows the same structure as the other task-based programs provided. First, the robot checks its current position and orientation with respect to the stick and the thermos. Then it performs the necessary actions to move the gripper and manipulate the objects until the task is completed. In this case, the robot needs to move to the stick, pick it up, move to the thermos, and use the stick to pull the thermos to the target location.