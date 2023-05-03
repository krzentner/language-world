# Steps:
    #  1. Move gripper in front of the button
    #  2. Move the gripper up against the wall
    #  3. Push the gripper into the button
    # First, move the gripper in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    # Next, move the gripper up against the wall (assuming we know exactly where
    # the wall is).
    if check("the gripper is not against the wall"):
        robot.move("gripper up against wall")
    # We should now be in position to push the gripper into the button.
    if check("the gripper is against the wall"):
        robot.push("gripper into button")