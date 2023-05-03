```
# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper to the left of the puck and close to the wall
    #  2. Move the gripper to the right of the puck and close to the wall
    #  3. Move the gripper above the puck and drop it around the puck
    #  4. Close the gripper around the puck
    #  5. Move the puck to the target
    # The wall is in the way, so we need to carefully maneuver the gripper to
    # get around the wall to grab the puck.
    # First, move the gripper to the left side of the puck and close to the wall.
    if check("the gripper is not left of the puck and close to the wall"):
        robot.move("gripper to left of puck and close to the wall")
    # Once the gripper is on the left side and close to the wall, move it to the
    # right side and close to the wall.
    if check("the gripper is not right of the puck and close to the wall"):
        robot.move("gripper to right of puck and close to the wall")
    # Now the gripper is on the right side and close to the wall. Move it above
    # the puck and drop it around the puck.
    if check("the gripper is not above the puck and dropped around it"):
        robot.move("gripper above puck")
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the gripper is near the puck and open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the gripper is above the puck and closed"):
        robot.place("puck at goal")
```