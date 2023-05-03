# Steps:
    #  1. Move the gripper to the left of the wall
    #  2. Move the gripper forward to the button
    #  3. Close the gripper around the button
    #  4. Push the button
    # We need to first move the gripper to the left of the wall so that it can
    # approach the button from the front
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # Once the gripper is to the left of the wall, we can move it directly
    # towards the button.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button", close_gripper=True)