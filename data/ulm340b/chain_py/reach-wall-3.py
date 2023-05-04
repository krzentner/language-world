
    # Steps:
    #  1. Reach towards the target
    #  2. Reach towards the target more carefully
    # If the gripper is not near the target location, move the gripper towards
    # it.
    if check("the robot's gripper is not near reach target"):
        robot.reach("to target")
    # If the gripper isn't near the target location, it's probably because we
    # hit the wall.
    # Move more carefully towards the goal.
    if check("the robot's gripper is not near reach target"):
        robot.reach("towards goal")

# pick-place-wall: pick up the puck and hold it at the target location, with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # Because this is "with a wall", the steps are the same as for 'pick-place',
    # except we try to grab the puck from above before putting the gripper
    # above the puck.
    # First, grab the puck from above in case the wall is in the way.
    # Otherwise, just reach above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper