# Steps:
    #  1. Line up the gripper as viewed from above, but further away than usual
    #  2. Move the gripper over the wall
    #  3. Lower the gripper onto the button
    #  4. Push down on the button
    # Because there's a wall in the way, we need to move the gripper over the
    # wall, which means moving it further away than usual.
    # Line up the robot's gripper from above, a bit further away than usual.
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not far enough away from the button"):
        robot.move("gripper further away from button and lined up above button")
    # Move the gripper over the wall.
    if check("the robot's gripper is not above the wall and the gripper is far enough away from the button"):
        robot.move("gripper over the wall")
    # Lower the gripper onto the button.
    if check("the robot's gripper is over the button and the gripper is not touching the button"):
        robot.drop("gripper onto button")
    # Push down on the button.
    if check("the robot's gripper is touching the button"):
        robot.push("down on button")