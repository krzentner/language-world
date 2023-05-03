

The steps of the program should be: 

1. Put gripper above the wall
2. Drop gripper above puck and onto wall
3. Close gripper around puck and hold wall in place
4. Move puck to goal

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the wall
    #  2. Drop gripper above puck and onto wall
    #  3. Close gripper around puck and hold wall in place
    #  4. Move puck to goal
    # First, put the gripper above the wall.
    if check("the robot's gripper is not above wall"):
        robot.put("gripper above wall")
    # If the gripper is not above the puck, drop the gripper onto the wall
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not above wall"):
        robot.drop("gripper above puck and onto wall")
    # If the gripper is near the puck, try to close it around the puck and
    # hold the wall in place.
    if check("the robot's gripper is near puck"):
        robot.close("gripper around puck and hold wall in place")
    # If the gripper is closed around the puck and holding the wall, we can
    # move the puck to the goal.
    if check("the robot's gripper is closed around puck and holding wall"):
        robot.place("puck at goal")
```