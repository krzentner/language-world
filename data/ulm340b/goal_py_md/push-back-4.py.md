

If you want to move the gripper to the right and downwards, you might write:

```
robot.move_gripper("forward right of the robot's gripper")
```

You can check the robot's state with a test, like:

```
if check("the puck is on the right side of the robot"):
    robot.move_gripper("on the left side of the robot")
```

In this way you can make the robot adapt to how it moved before.
Here are some more tests you can use:

```
if check("the puck is left of the robot"):
    robot.move_gripper("right of the puck")
if check("the puck is behind the robot"):
    robot.move_gripper("on top of the puck")
if check("the puck is in front of the robot"):
    robot.move_gripper("on top of the puck")
if check("the puck is left of the robot and the puck is far away"):
    robot.move_gripper("left of the puck")
if check("the puck is left of the robot and the puck is not far away"):
    robot.move_gripper("left of the puck")
if check("the puck is in front of the robot and the puck is far away"):
    robot.move_gripper("in front of the puck")
if check("the puck is in front of the robot and the puck is not far away"):
    robot.move_gripper("in front of the puck")
if check("the puck is behind the robot and the puck is far away"):
    robot.move_gripper("behind the puck")
if check("the puck is behind the robot and the puck is not far away"):
    robot.move_gripper("behind the puck")
if check("the puck is right of the robot"):
    robot.move_gripper("left of the puck")
if check("the puck is above the robot"):
    robot.move_gripper("below the puck")
if check("the puck is below the robot"):
    robot.move_gripper("above the puck")
if check("the puck is on top of the robot"):
    robot.move_gripper("below the puck")
if check("the puck is below the robot and the puck is far away"):
    robot.move_gripper("below the puck")
if check("the puck is below the robot and the puck is not far away"):
    robot