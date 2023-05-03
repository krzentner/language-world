Here's the program for the `sweep` task:

```
# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        if check("the gripper is not positioned correctly to sweep the cube"):
            robot.move("gripper to side of cube")
        robot.slide("the cube to the goal")
``` 

This code assumes that there is a `check` function that returns `True` if the condition passed as argument is satisfied, and `False` otherwise. The `robot` object has several methods that allow it to manipulate the gripper and perform specific actions. The `sweep` function first uses the `place` and `drop` methods to correctly position the gripper around the cube. Once the gripper is closed around the cube, it uses the `move` method to position the gripper correctly to sweep the cube sideways, before finally using the `slide` method to move the cube to the goal location.