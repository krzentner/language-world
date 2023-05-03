# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal while avoiding the wall
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper, but we need to make sure we don't push the puck
    # into the wall.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # Check if there's a wall blocking the way
        if check("there is a wall blocking the puck"):
            # If there is a wall, move the gripper around the wall to avoid it
            robot.move_gripper("above the wall", close_gripper=True)
            robot.move_gripper("beside the puck and beyond the wall")
        else:
            robot.move_gripper("above the target location")