
    # Steps:
    #  1. Put gripper in front of door handle
    #  2. Push the door handle to the right
    # If the gripper is not near the door handle, move it there.
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    # If the gripper is near the door handle, we can try to push it.
    if check("the robot's gripper is near door handle"):
        robot.push("door handle right")

# pick-place-wall: pick up the puck and hold it at the target location, with
#   the gripper against the wall behind it
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
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
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# wall-push: push the puck against the wall
def wall_push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2