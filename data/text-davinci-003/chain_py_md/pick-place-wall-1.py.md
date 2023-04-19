

Steps:
1. Line up the gripper with the wall
2. Put the gripper above the puck
3. Drop the gripper around the puck
4. Close the gripper around the puck
5. Move the puck to goal

# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Line up the gripper with the wall
    #  2. Put the gripper above the puck
    #  3. Drop the gripper around the puck
    #  4. Close the gripper around the puck
    #  5. Move the puck to goal
    # First, line up the gripper with the wall.
    if check("the robot's gripper is not horizontally aligned with the wall"):
        robot.align("gripper to the wall")
    # Put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal, keeping the short wall in between.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the puck is below the robot's gripper"):
        robot.place("puck at goal")