
    # Steps:
    #  1. Put gripper near the top of the puck
    #  2. Close gripper around the puck
    #  3. Lift the puck up
    #  4. Move the puck to the goal
    # First, move the gripper near the top of the puck.
    if check("the robot's gripper is not near the top of the puck"):
        robot.move("gripper near top of puck")
    # If the gripper is near the top of the puck but open, maybe we can grab it
    # by closing the gripper.
    if check("the robot's gripper is near the top of the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the puck.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near top of puck and the robot's gripper is closed"):
        robot.lift("puck up")
    # If the puck is lifted up, we can move it to the goal.
    if check("the puck is lifted up"):
        robot.move("puck to goal")