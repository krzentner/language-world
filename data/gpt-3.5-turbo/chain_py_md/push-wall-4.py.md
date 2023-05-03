# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal, including going over the small wall
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the goal location, including potentially going over the small
    # wall if necessary.
    # Close the gripper to make sure we keep control of the puck.
    while not check("the puck has arrived at the goal location"):
        if check("the puck is blocked by a small wall"):
            # If the gripper is above the small wall, slide the puck forward while
            # keeping pressure on it with the gripper to try to get it over the wall.
            if check("the robot's gripper is above the small wall"):
                robot.slide("the puck to the goal")
            # If the gripper is blocked by a small wall, move it to the side and try
            # to slide the puck forward again.
            else:
                robot.move("the gripper to the side of the wall")
        else:
            robot.slide("the puck to the goal")