

Use only one `check` function:

```
if check("stick is not vertically aligned with the robot's gripper and thermos is not vertically aligned with the robot's gripper"):
    robot.grab("stick")
```

And also use only one `place` function:

```
if check("thermos is near target"):
    robot.place("thermos at target")
```


-->

def stick_pull(robot):
    # stick-pull: grab the stick and use it to pull the thermos to the target location
    if check("stick is not vertically aligned with the robot's gripper and thermos is not vertically aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is not vertically aligned with the thermos"):
        robot.drop("stick below thermos")
    if check("the robot's gripper is forward aligned with the thermos"):
        robot.pull("thermos away from wall")
    if check("thermos is near target"):
        robot.place("thermos at target")
    if check("stick is not vertically aligned with the robot's gripper"):
        robot.put("stick under robot gripper")
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.grab("stick")
    if check("the robot's gripper is vertically aligned with the stick"):
        robot.drop("stick below robot gripper")

    # def button_press_topdown(robot):
    #     if check("the robot's gripper is not vertically aligned with button"):
    #         robot.put("gripper above button")
    #     if check("the robot's gripper is vertically aligned with button"):
    #         robot.push("down on button")

    # def drawer_close(robot):
    #     if check("the robot's gripper is not near the drawer handle"):
    #         robot.grab("drawer handle")
    #     if check("the robot's gripper is forward aligned with drawer handle"):
    #         robot.push("drawer closed")

    # def drawer_open(robot):
    #     if check("the robot's gripper is not vertically aligned with drawer handle"):
    #         robot.put("gripper above drawer handle")
   