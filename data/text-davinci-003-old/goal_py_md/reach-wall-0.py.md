

Steps:
 1. Reach towards the wall
 2. Move the gripper up, over the wall
 3. Reach towards the target

We need to start by moving towards the wall. The first move while reaching towards the wall should be slightly steeper than the move towards the target location.

```
# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach towards the wall
    #  2. Move the gripper up, over the wall
    #  3. Reach towards the target
    if check("the robot's gripper is not near reach wall"):
        robot.move_gripper("near the wall", steeper=True)
```

Now that the robot is near the wall, the robot can move it's gripper over the wall and towards the target location.

```
# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach towards the wall
    #  2. Move the gripper up, over the wall
    #  3. Reach towards the target
    if check("the robot's gripper is not near reach wall"):
        robot.move_gripper("near the wall", steeper=True)
    # Move the gripper above the wall, so that it can reach over the wall.
    if check("the robot's gripper is at the wall"):
        robot.move_gripper("above the wall")
    # Now that the gripper is above the wall, move it to the target location.
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("near the target location")
```