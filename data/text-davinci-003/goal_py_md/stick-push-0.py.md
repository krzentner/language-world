

```
# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    #  1. Put gripper near the stick
    #  2. Grab the stick
    #  3. Move the stick to above the thermos
    #  4. Push the thermos to the target location
    # First, put the gripper near the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick")
    # Once the gripper is near the stick, close the gripper and grab the stick.
    if check("the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Line the stick up above the thermos.
    if check("the stick is not above the thermos"):
        robot.move_gripper("above the thermos")
    # Push the thermos towards the target location.
    if check("the stick is above the thermos"):
        robot.move_gripper("above the target location")
```