# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    #  4. If puck hits wall, move gripper around wall and continue sliding
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper, but there's a small wall in the way that we
    # need to get around.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # Slide the puck toward the goal until we hit the wall.
        while not check("the puck has hit the wall"):
            robot.slide("the puck toward the goal")
        # If we hit the wall, move the gripper around it.
        if check("the puck has hit the wall"):
            robot.move("gripper around the wall")
        # Continue sliding the puck to the goal.
        robot.slide("the puck to the goal")