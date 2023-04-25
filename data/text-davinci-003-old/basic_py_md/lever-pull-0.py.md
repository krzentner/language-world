

Then add the code:

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not around the lever"):
        robot.grab("gripper around lever")
    if check("the robot's gripper is around the lever"):
        robot.pull("lever up")
``