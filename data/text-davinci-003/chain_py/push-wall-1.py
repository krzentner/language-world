
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck against wall
    #  4. Slide puck away from wall
    # We need to trap the puck between the gripper and the wall in order to
    # slide the puck.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it against the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck against the wall")
    # Once the wall is pushing back against the robot, it's pushing the puck, so
    # slide the puck away from the wall.
    if check("the wall is pushing back against the robot"):
        robot.slide("the puck away from the wall")