# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck towards the wall
    #  4. Push against the wall to move the puck around it
    #  5. Slide the puck to the goal
    # We can follow the same steps as the regular push function, with the
    # additional step of pushing against the wall to move the puck around it.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it towards the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck towards the wall")
    # Once the puck is near the wall, push against the wall to move the puck
    # around it.
    if check("the puck is near the wall and the robot's gripper is touching the wall"):
        robot.push("against the wall")
    # Finally, slide the puck towards the goal.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")