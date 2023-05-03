# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Push the gripper into the top of the puck
    #  3. If the gripper is not behind the wall, move the gripper around the wall
    #  4. Slide the puck to the goal
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # To slide the puck past the wall, we need to trap the puck by pushing down
    # on it from above, and move the gripper to slide it.
    # If the gripper is not aligned with the puck, move it down to the puck to
    # trap it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is aligned with the puck but not near it, push it down to
    # trap the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("gripper into the puck")
    # If the gripper has trapped the puck, check if it's behind the wall.
    if check("the robot's gripper has trapped the puck and the puck is behind the wall"):
        robot.slide("the puck to the goal")
    # If the gripper has trapped the puck, but it's still in front of the wall,
    # we need to move the gripper around the wall.
    if check("the robot's gripper has trapped the puck and the puck is in front of the wall"):
        robot.move("gripper around wall")
        # After moving the gripper around the wall, if the puck is still trapped
        # we can slide it to the goal.
        if check("the robot's gripper has trapped the puck and the puck is behind the wall"):
            robot.slide("the puck to the goal")