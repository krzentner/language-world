# Steps:
    #  1. Move the gripper above the wall
    #  2. Move the gripper to the target location
    # We can't move the gripper directly to the target location because there is
    # a wall in the way, so we need to move it above the wall first.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Once the gripper is above the wall, we can move it to the target location.
    if check("the robot's gripper is above the wall and not at the target location"):
        robot.move_gripper("near the target location")