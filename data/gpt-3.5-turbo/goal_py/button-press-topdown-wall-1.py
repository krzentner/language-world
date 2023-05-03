# Steps:
    #  1. Line up the gripper as viewed from above, on the other side of the wall
    #  2. Close the gripper around the button
    #  3. Move the gripper and button together towards the wall
    #  4. Move the gripper and button along the wall until gripper is over the button
    #  5. Line up gripper directly over the button
    #  6. Push down on the button from the top
    # Because there is a wall in the way, we need to move the gripper and button
    # along the wall until we can get the gripper above the button.
    # First line up the gripper on the other side of the wall from where the
    # button is.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button on the other side of the wall")
    # Once the gripper is lined up on the other side of the wall, close it around
    # the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not around button"):
        robot.move_gripper("around the button")
    # Now move the gripper and button together towards the wall.
    # When the wall is in front of us and the button is on the other side, we
    # should just move forward.
    if check("the wall is directly in front of the robot's gripper and the button is on the other side of the wall"):
        robot.move_forward()
    # If the wall is not directly in front of us, we need to move to the right
    # until we are lined up.
    if check("the wall is not directly in front of the robot's gripper"):
        robot.move_gripper("right of the wall", close_gripper=True)
    # Once the gripper is lined up with the wall, move it along the wall until
    # the gripper is over the button.
    if check("the robot's gripper is not over the button"):
        robot.move_gripper("over the button")
    # Finally, line up the gripper directly over the button and push down on the button.
    if check("the robot's gripper is over the button"):
        robot.move_gripper("near the button", close_gripper=True)