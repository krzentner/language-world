# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube
    #  3. Move the cube to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    # If the gripper is not around the cube, grab it.
    if check("the robot's gripper is not around the cube"):
        robot.grab("cube")
    # Move the cube to the target location by sliding it sideways.
    if check("the robot's gripper is holding the cube"):
        robot.slide("the cube to the target location")