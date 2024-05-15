# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into bottom of puck
    #  3. Slide puck backwards to goal
    # The robot can slide the puck backwards by trapping it by pushing up on it
    # from below and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("below the puck", close_gripper=True)
    # If the gripper is below the puck, we've probably trapped the puck and can
    # slide it backwards to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
        robot.move_gripper("above the target location")