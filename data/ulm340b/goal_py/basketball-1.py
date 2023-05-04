
    # Steps:
    #  1. Put the gripper right above the ball
    #  2. Put the gripper above the ball
    #  3. Pick up the ball
    #  4. Move the ball into the goal
    # The first step is to put the gripper right above the ball.
    if check("the robot's gripper is not vertically aligned with ball"):
        robot.move_gripper("vertically aligned with ball", close_gripper=True)
    # Then, we put the gripper above the ball.
    if check("the robot's gripper is vertically aligned with ball"):
        robot.move_gripper("almost vertically aligned with ball")
    # If the gripper is aligned with the ball from above, pick up the ball.
    if check("the robot's gripper is above ball"):
        robot.move_gripper("above the ball")
    # The final step is to move the ball into the goal
    if check("the robot's gripper is above ball"):
        robot.move_gripper("vertically aligned with ball")

# button-press: push the button down
def button_press(robot):
    # Steps:
    #  1. Move the robot gripper near the button
    #  2. Move the robot gripper down
    # To press the button, we first move the gripper to near the button.
    if check("the robot's gripper is not near button"):
        robot.move_gripper("near button")
    # Once the gripper is near the button, we move the gripper down, so that the
    # button is pressed.
    if check("the robot's gripper is near button"):
        robot.move_gripper("vertically aligned with the robot's gripper")

# lever-pull: push the lever down
def lever_pull(robot):
    # Steps:
    #  1. Move the robot gripper near the lever
    #  2. Pull the robot gripper down, pulling the lever down
    # To press the lever, we first move the gripper to near the lever.
    if check("the robot's gripper is not near lever"):
        robot.move_gripper("near lever")
    # Once the gripper is near the lever, we move the gripper down,