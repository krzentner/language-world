# Steps:
    #  1. Adjust the gripper to a lower height to go over the wall
    #  2. Line up the gripper as viewed from above
    #  3. Push down on the button from the top
    # Because there is a wall in the way, we need to adjust the gripper height to
    # go over it before lining up the gripper from above and pushing down on the button.
    # Adjust the gripper to a lower height
    if check("the robot's gripper is not at a lower height"):
        robot.move_gripper("lower height", close_gripper=True)
    # Line up the robot's gripper from above
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Push down on the button
    if check("the robot's gripper is aligned with the button"):
        robot.move_gripper("near the button")