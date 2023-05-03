
    # Steps:
    #  1. Line up the gripper with the button
    #  2. Lower the gripper over the wall
    #  3. Push down on the button from the top
    # First, line up the gripper with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the gripper is lined up with the button but there is still a wall in
    # the way, move the gripper over the wall.
    if check("the robot's gripper is vertically aligned with the button and there is a wall in the way"):
        robot.move_gripper("near the button")
    # If the gripper is close to the button and the wall is out of the way, we
    # can push down on the button.
    if check("the robot's gripper is near the button and there is no wall in the way"):
        robot.move_gripper("below the button")