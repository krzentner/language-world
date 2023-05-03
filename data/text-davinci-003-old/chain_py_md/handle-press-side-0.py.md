

Step 1: Line Up Gripper From the Side

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Line up the gripper from the side
    #  2. Push down on the handle from the side
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.align("gripper to handle from side")
```

Step 2: Push Down the Handle

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Line up the gripper from the side
    #  2. Push down on the handle from the side
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.align("gripper to handle from side")
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on the handle")
```