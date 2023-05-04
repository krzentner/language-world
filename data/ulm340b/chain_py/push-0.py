
    # Steps:
    #  1. Put gripper above puck
    #  2. Slide puck to goal
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    # If the gripper is above puck, push it to the goal.
    if check("the robot's gripper is above puck"):
        robot.push("puck to goal")

# pick-place-wall: pick up the puck and hold it near the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Place puck above the wall
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
    # Try to place the puck on the wall.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck on wall")

# reach-wall: reach to the wall
def reach_wall(robot):
    # Steps:
    #  1. Reach towards the wall
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the wall
 