

We'll need to think of a way to get around the wall, since the robot has a single gripper. 

First, the robot should put the gripper above the puck, so that it doesn't accidently bump the wall while trying to grab the puck.

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper around the wall
    #  3. Drop gripper around puck
    #  4. Close gripper around puck
    #  5. Move puck to goal
    # First, put the gripper above the puck, so that we don't bump the wall. 
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
```

Next, the robot should move the gripper around the wall, so that it is able to grab the puck. It should move the gripper to the left of the wall, so it can grab the puck from the right side. 

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper around the wall
    #  3. Drop gripper around puck
    #  4. Close gripper around puck
    #  5. Move puck to goal
    # First, put the gripper above the puck, so that we don't bump the wall.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # Next, move the gripper to the left of the wall, so the robot can grab the puck from the right side.
    if check("the robot's gripper is not to the left of the wall"):
        robot.move_gripper("to the left of the wall")
``` 

Now that the gripper is in position, the robot should drop it around the puck so it can be grabbed. 

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper around the wall
    #  3. Drop gripper around puck
    # 