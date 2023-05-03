

Then add the code:

```
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot and there is a wall on the right of the puck"):
        robot.slide("the puck to the left of the wall")
    if check("the wall is now on the left of the puck"):
        robot.push("the puck to the goal")
```