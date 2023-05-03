# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into bottom of puck
    #  3. Slide puck backwards to goal
    # This task is similar to the "push" task, but we need to push the puck
    # backwards instead of forwards.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the bottom of the puck, we can trap the puck by
    # pushing up on it and slide it backwards to the target location.
    if check("the robot's gripper is above the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")