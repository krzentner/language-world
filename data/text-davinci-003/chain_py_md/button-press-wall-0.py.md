

Steps:
1. Line up the gripper with the button as viewed from the front
2. Push the wall from the side to clear the way
3. Push the button from the front

If the robot's gripper is not vertically aligned with the button, we should move the gripper near the button to start pushing.

```
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper near button")
```

If the gripper is near the button, but the wall is blocking the button, we should move the gripper to the side of the wall and push the wall away.

```
    if check("the robot's gripper is near the button and the wall is blocking the button"):
        robot.push("wall away")
```

Once the wall is moved out of the way, we can just push the button from the front.

```
    if check("the robot's gripper is near the button and the wall is not blocking the button"):
        robot.push("button from front")
```