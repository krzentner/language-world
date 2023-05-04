

and use the instructions above to complete the program.

Here are some useful checks you can use:

```
check("the soccer ball is left of the robot's gripper")
check("the soccer ball is right of the robot's gripper")
check("the robot's gripper is below the soccer ball")
check("the robot's gripper is above the soccer ball")
check("the robot's gripper is vertically aligned with the soccer ball")
check("the robot's gripper is almost vertically aligned with the soccer ball")
check("the robot's gripper is in front of the soccer ball")
check("the robot's gripper is near the soccer ball")
check("the soccer ball is below the robot's gripper")
check("the soccer ball is above the robot's gripper")
check("the soccer ball is behind the robot's gripper")
check("the soccer ball is in front of the robot's gripper")
check("the soccer ball is near the robot's gripper")
```

Here are some useful actions you can use:

```
robot.move("gripper to left of soccer ball")
robot.move("gripper to right of soccer ball")
robot.move("gripper below soccer ball")
robot.move("gripper above soccer ball")
robot.put("gripper to left of soccer ball")
robot.put("gripper to right of soccer ball")
robot.put("gripper below soccer ball")
robot.put("gripper above soccer ball")
robot.slide("soccer ball left")
robot.slide("soccer ball right")
robot.push("soccer ball left")
robot.push("soccer ball right")
robot.push("soccer ball harder")
```
"""

# soccer: push the soccer ball into the target location
def soccer(robot):
    # If the soccer ball is not near the robot's gripper, put the gripper near the soccer ball.
    if check("the soccer ball is left of the robot's gripper"):
        robot.move("gripper to left of soccer ball")
    if check("the soccer ball is right of the robot's gripper"):
        robot.move("gripper to right of soccer ball")
    if check("the soccer ball is below the robot's gripper"):
        robot.move("gripper below soccer ball")
    if check("the soccer ball is above the robot's gripper"):
        robot.move("gripper above soccer ball")
    # if the soccer ball is near the robot's gripper and the gripper is behind the soccer ball