



```

```

## Write a program that moves the robot's gripper to the goal.

```
robot.move_gripper("above the puck")
```

```

```

## Align the gripper with the puck vertically.

```
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")
```

```

```

## Align the gripper with the puck horizontally.

```
if check("the robot's gripper is not forward aligned with the puck"):
    robot.move_gripper("forward aligned with the puck")
```

```

```

## Align the gripper with the puck both vertically and horizontally.

```
if check("the robot's gripper is not vertically aligned with the puck"):
    robot.move_gripper("vertically aligned with the puck")

if check("the robot's gripper is not forward aligned with the puck"):
    robot.move_gripper("forward aligned with the puck")
```

```

```

## Open the gripper to try to grab the puck.

```
robot.move_gripper("above the puck")

if check("the robot's gripper is above the puck and the robot's gripper is open"):
    robot.move_gripper("around the puck")
```

```

```

## Open the gripper and drop it down on the puck to try to grab it.

```
if check("the robot's gripper is above the puck"):
    robot.move_gripper("almost around the puck")
    robot.move_gripper("around the puck", close_gripper=True)
```

```

```

## Open the gripper and drop it down on the puck. If the gripper is still not aligned with the puck horizontally, put the gripper in front of the puck.

```
if check("the robot's gripper is above the puck"):
    robot.move_gripper("around the puck", close_gripper=True)

if check("the robot's gripper is not forward aligned with the puck"):
    robot.move_gripper("forward aligned with the puck")
```

```

```

## Open the gripper and drop it down on the puck. If the gripper is still not aligned with the puck vertically, put the gripper above the puck.

```
if check("the robot's