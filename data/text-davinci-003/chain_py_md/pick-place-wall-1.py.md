

The steps of the task are as follows:

1. Put gripper above puck
2. Drop gripper into the pocket formed between the puck and the wall
3. Close gripper around puck 
4. Move puck to goal

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper into the pocket formed between the puck and the wall
    #  3. Close gripper around puck 
    #  4. Move puck to goal
    # First, put the gripper above the puck to avoid bumping the puck while trying
    # to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # Once the gripper is above the puck, adjust it to drop it into the pocket
    # formed between the puck and the wall.
    if check("the robot's gripper is above the puck and the robot's gripper is not in the pocket between the puck and the wall"):
        robot.place("gripper in pocket between puck and wall")
    # If the gripper is in the pocket and open, close the gripper around the
    # puck.
    if check("the robot's gripper is in pocket between puck and wall and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We've closed the gripper around the puck, so we may have trapped the puck.
    # Try to move it to the target location.
    if check("the robot's gripper is in pocket between puck and wall and the robot's gripper is closed"):
        robot.place("puck at goal")
```