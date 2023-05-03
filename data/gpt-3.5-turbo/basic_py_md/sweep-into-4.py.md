Sure, here's the code for the `sweep-into` task:

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        if check("the cube is to the left of the robot's gripper"):
            robot.put("gripper to the right of the cube")
        robot.slide("cube to the target location")
``` 

This code will execute the sweeping motion to pick up the cube, align it to the target direction, and move it to its target location. Let me know if you have any more questions!