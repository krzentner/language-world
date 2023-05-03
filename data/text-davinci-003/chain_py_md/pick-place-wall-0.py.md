

Now, we need to pick up the puck, but there is a short wall in the way. We’ll need to use the same steps we would to pick up the puck without a wall. The steps are:

1. Put gripper above puck
2. Drop gripper around puck
3. Close gripper around puck
4. Move puck to goal

However, to do so, we must first align the gripper correctly with the puck, making sure it is high enough to not hit the wall in the way.

1. Put gripper above wall
2. Drop gripper to the side of the wall
3. Move gripper above puck, ensuring it is high enough to not hit the wall
4. Drop gripper around puck
5. Close gripper around puck
6. Move puck to goal


```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above wall
    #  2. Drop gripper to the side of the wall
    #  3. Move gripper above puck, ensuring it is high enough to not hit the wall
    #  4. Drop gripper around puck
    #  5. Close gripper around puck
    #  6. Move puck to goal
    # First, put the gripper slightly above the wall.
    if check("the robot's gripper is not above wall and the robot's gripper is not vertically aligned with the wall"):
        robot.put("gripper above wall")
    # Next, drop the gripper to the side of the wall.
    if check("the robot's gripper is not to the side of the wall and the robot's gripper is not vertically aligned with the wall"):
        robot.put("gripper to the side of the wall")
    # Now that the gripper is lined up, move it above the puck, making sure it is high enough to not hit the wall.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper at puck, ensuring it is highEnough above wall")
    # If the gripper is lined up above the puck but not near it, move the gripper
    # down to the puck to grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # grab