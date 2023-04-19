# Steps:
    # 1. Put gripper above button but not too high due to wall
    # 2. Move forward until gripper touches the wall
    # 3. Move gripper towards button to press it down
    # Because there's a wall blocking the path, we need to be careful about how
    # we approach the button.
    # First, line up the gripper above the button, but make sure it's not too
    # high to avoid hitting the wall.
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
    # Now we can move forward until we hit the wall.
    if check("the robot's gripper is not touching the wall"):
        robot.move_forward_until_touch("the wall")
    # Once we're touching the wall, we can move the gripper forward to press
    # the button.
    if check("the robot's gripper is touching the wall and is not near the button"):
        robot.move_gripper("near the button")