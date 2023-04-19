
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube sideways to goal
    # Put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, drop it around the cube.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, grab it by closing the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so we
    # probably grabbed it.
    # Try to move the cube sideways to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.sweep("cube towards goal")