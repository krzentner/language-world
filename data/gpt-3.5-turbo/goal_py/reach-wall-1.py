# Steps:
    #  1. Move the gripper above the wall
    #  2. Move the gripper to the target location
    #  3. Drop the gripper down to the target location
    # If the robot's gripper is not above the wall, move it there first.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # If the gripper is above the wall but not at the target location, move it
    # to the target location.
    if check("the robot's gripper is above the wall and the gripper is not at the target location"):
        robot.move_gripper("near the target location")
    # Finally, drop the gripper down to the target location.
    # We assume the gripper can fit through any gap in the wall.
    if check("the robot's gripper is not at the target location"):
        robot.move_gripper("at the target location", close_gripper=True)