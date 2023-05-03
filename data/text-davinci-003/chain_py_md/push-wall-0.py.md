

# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into the puck
    #  3. Slide puck to the wall
    #  4. Push gripper into side of wall
    #  5. Slide puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("puck to wall")
    # Now that the puck is near the wall, the gripper can trap it by pushing
    # into the side of the wall.
    if check("the robot's gripper is above the wall and the robot's gripper is not near wall"):
        robot.push("gripper into wall")
    # Once the wall is trapping the puck, we can safely move the puck to the
    # target location without fear of it getting away.
    if check("the robot's gripper is near the wall and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")