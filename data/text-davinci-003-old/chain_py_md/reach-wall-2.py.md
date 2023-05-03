

Then,

```
# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach up above the wall
    #  2. Reach around the wall to the desired target
    # If the robot's gripper is not above the wall, move it up above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.reach("above the wall")
    # Try to reach around the wall to the target location.
    if check("the robot's gripper is above the wall"):
        robot.reach("around the wall to goal")
```