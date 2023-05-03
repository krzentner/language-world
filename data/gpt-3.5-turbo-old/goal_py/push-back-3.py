# Steps:
    # 1. Put gripper above puck
    # 2. Push gripper into back of puck
    # 3. Slide puck to goal
    # Similar to "push", but we're pushing the puck backwards instead of forwards
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is above the puck and the robot's gripper is not near the back of the puck"):
        robot.move_gripper("almost vertically aligned with the back of the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    if check("the robot's gripper is almost vertically aligned with the back of the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")