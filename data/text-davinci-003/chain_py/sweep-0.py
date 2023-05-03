
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Push cube over goal
    #  5. Move gripper down slightly
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to push the cube to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.push("cube over goal")
    # If the cube is over the goal, move the gripper down slightly to make sure
    # the cube stays in the goal.
    if check("the cube is over the goal"):
        robot.put("gripper down slightly")