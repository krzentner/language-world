# Steps:
    #  1. Move the robot so that the gripper is aligned with the button
    #  2. Extend the gripper towards the button
    #  3. Push the button
    # The main challenge here is that there is a wall in the way, so we need to
    # make sure we don't try to push through it.
    # First, move the robot as close to the wall as possible and in front of the
    # button.
    if check("the robot is not in front of the button"):
        robot.move("in front of the button")
    # If the gripper isn't aligned with the button, rotate the robot to face it.
    if check("the robot is not facing the button"):
        robot.rotate("towards the button")
    # Make sure the gripper is close to the button.
    if check("the robot's gripper is not close to the button"):
        robot.move_gripper("near the button")
    # Finally, push the button by extending the gripper while keeping it in
    # contact with the button.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("pushing the button")