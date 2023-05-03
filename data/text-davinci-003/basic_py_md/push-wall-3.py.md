

Then, write the code:

```
# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck and the small wall is not below the robot's gripper"):
        robot.put("the gripper above the puck and position the small wall below the gripter")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck and the small wall is below the robot's gripper"):
        robot.push("the gripper into the puck and push the wall away")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
```