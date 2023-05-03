

Then the code:

```
    if check("the robot's gripper is not forward aligned with the button and the wall is not horizontally aligned with the robot's gripper"):
        robot.align("gripper to button")
    if check("the wall is horizontally aligned with the robot's gripper and the button is not vertically aligned with robot's gripper"):
        robot.align("button to robot's gripper")
    if check("the button is vertically aligned with robot's gripper"):
        robot.push("robot's gripper towards button")
```