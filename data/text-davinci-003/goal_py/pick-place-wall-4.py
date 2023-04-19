
    # Steps:
    #  1. Put gripper above the puck
    #  2. Lift the gripper up, so that it's over the short wall
    #  3. Drop gripper around puck
    #  4. Close gripper around puck
    #  5. Move puck to goal
    # We need to put the gripper above the puck before we can grab it,
    # but because of the short wall we also need to lift the gripper up.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("almost vertically aligned with the puck", lift=True)
    # As long as the gripper is almost lined up and up, we can just drop it
    # around the top of the puck to trap it.
    if check("the robot's gripper is almost vertically aligned with the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is closed around the puck, we can move it to the target
    # location.
    if check("the robot's gripper is closed around the puck"):
        robot.move_gripper("above the target location")