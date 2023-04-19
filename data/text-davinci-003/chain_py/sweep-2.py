
    # Steps:
    #  1. Put gripper above cube
    #  2. Open gripper and move it around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    # Since the gripper isn't totally above the cube, we should open it and move
    # it all the way around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move("gripper around cube")
    # Now that the robot's gripper is around the cube, close it.
    if check("the robot's gripper is around the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is inside the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move("cube to the goal")