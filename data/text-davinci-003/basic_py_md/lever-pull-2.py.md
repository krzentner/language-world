

Your code should look like this:
```
# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is horizontally aligned with the lever and the robot's gripper is not near the lever"):
        robot.move("gripper near lever")
    if check("the robot's gripper is near the lever"):
        robot.push("lever up")
```