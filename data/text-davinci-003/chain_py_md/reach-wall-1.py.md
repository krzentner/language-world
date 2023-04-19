

The robot needs to reach the target location, which is blocked by a short wall.

Steps:
1. Reach towards the target location, until the wall is detected. 
2. Move the gripper around the wall, to the other side. 
3. Reach towards the target location, until it is reached.

```
# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach towards the target location, until the wall is detected.
    if check("the target is not reached and the wall is not detected"):
        robot.reach("to target location")
    #  2. Move the gripper around the wall, to the other side.
    if check("the target is not reached and the wall is detected"):
        robot.move("gripper around wall")
    #  3. Reach towards the target location, until it is reached.
    if check("the wall is not detected and the target is not reached"):
        robot.reach("to target location")
```