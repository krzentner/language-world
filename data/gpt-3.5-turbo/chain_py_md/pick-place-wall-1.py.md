# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):

Here's an implementation of `pick_place_wall`:

```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Move gripper to slightly above puck
    #  2. Check if wall is in the way
    #  3. If wall is in the way, move gripper to edge of wall and lower gripper to reach puck
    #  4. Grab puck
    #  5. If wall is in the way, lift gripper above wall and move gripper to goal
    #  6. If wall is not in the way, move gripper to goal and drop puck
    # First, put the gripper slightly above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper above puck slightly")
    # Check if the wall is in the way.
    wall_in_way = check("wall is in the way of robot's gripper and puck")
    # If the wall is in the way, move the gripper to the edge of the wall and
    # lower it to reach the puck.
    if wall_in_way and check("the robot's gripper is not at edge of wall"):
        robot.move("gripper to edge of wall")
    if wall_in_way and check("the robot's gripper is not low enough to reach puck"):
        robot.lower("gripper to reach puck")
    # Grab the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.grab("puck")
    # If the wall was in the way, lift the gripper above the wall and move it
    # to the goal.
    if wall_in_way and check("the robot's gripper is not above the wall"):
        robot.move("gripper above wall")
    if wall_in_way and check("the robot's gripper is not above goal"):
        robot.move("gripper above goal")
    # If the wall was not in the way, just move the gripper to the goal and drop
    # the puck.
    if not wall_in_way and check("the robot's gripper is not above goal"):
        robot.move("gripper above goal")
    if check("the robot's gripper is above goal"):
        robot.drop("puck at goal")
```