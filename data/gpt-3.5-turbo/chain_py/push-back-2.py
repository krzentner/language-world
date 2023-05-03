# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into bottom of puck
    #  3. Slide puck backwards to goal
    # To push the puck backwards instead of forwards, we'll need to push into the
    # bottom of the puck instead of the top.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to push it backwards.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the bottom of the puck")
    # If the gripper is near the puck and pushing into the bottom of it, we've
    # probably trapped the puck and can slide it backwards to the target
    # location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the robot's gripper is pushing into the bottom of the puck"):
        robot.slide("the puck backwards to the goal")