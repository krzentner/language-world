

Steps:
1. Put gripper above the head of the hammer
2. Drop the gripper around the head of the hammer
3. Close the gripper around the head of the hammer
4. Line up the hammer with the nail
5. Swing the hammer down onto the nail

If the robot's gripper isn't above the head of the hammer, move it above the hammer.

```
if check("the robot's gripper is not above the head of the hammer"):
    robot.move_gripper("above the head of the hammer")
```

If the gripper isn't around the head of the hammer and is open, close the gripper around the hammer.

```
if check("the robot's gripper is not around the head of the hammer and the gripper is open"):
    robot.move_gripper("near the head of the hammer", close_gripper=True)
```

If the gripper is around the hammer, line up the hammer with the nail.

```
if check("the robot's gripper is around the head of the hammer"):
    robot.move_gripper("vertically aligned with the nail")
```

Once the hammer is lined up with the nail, the robot can swing the hammer down onto the nail.

```
if check("the robot's gripper is vertically aligned with the nail"):
    robot.move_gripper("below the nail", close_gripper=False)
```