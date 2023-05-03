# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to wall
    #  4. Lift gripper until clear of wall
    #  5. Push the puck to the goal
    # The robot needs to use a little more finesse to slide the puck past the wall.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
      
        robot.slide("the puck to the wall")
        # Once the puck has reached the wall, we need to move the gripper up until
        # it clears the wall.
        if check("the puck has reached the wall"):
            robot.lift("the gripper to clear the wall")
            # Once the gripper has cleared the wall, we can push the puck to the goal.
            if check("the gripper has cleared the wall"):
                robot.push("the puck to the goal")