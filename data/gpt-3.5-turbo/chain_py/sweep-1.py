# Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around cube
    #  3. Close the gripper around cube
    #  4. Move the gripper and cube to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above the cube")
    # If the gripper is not around the cube, put the gripper around it.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Move the gripper and cube to the target location by sliding it sideways.
    # If we didn't grab the cube, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.slide("gripper and cube to the goal")