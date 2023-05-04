
    # Steps:
    #  1. Put gripper below the ball
    #  2. Grab the ball with the gripper
    #  3. Line the ball up with the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper below the ball.
    if check("the robot's gripper is not horizontally aligned with the ball"):
        robot.move_gripper("below the ball")
    # As long as the gripper is mostly vertically aligned with the ball, it
    # should be able to grab it by closing the gripper.
    if check("the robot's gripper is above the ball and the ball is below the robot's gripper"):
        robot.move_gripper("above the ball", close_gripper=True)
    # Now that the ball is in the gripper, line the ball up with the hoop.
    if check("the ball is above the hoop and the robot's gripper is below the hoop"):
        robot.move_gripper("vertically aligned with the hoop")
    # Once the ball is lined up with the hoop, drop the ball into the hoop.
    if check("the robot's gripper is vertically aligned with the hoop"):
        robot.move_gripper("below the hoop")

# button-press-topdown-v1: push the button down from above
def button_press_topdown_v1(robot):
    # Steps:
    #  1. Put gripper vertically aligned with button
    #  2. Lower gripper into button
    #  3. Move gripper to above the button
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with button")

# button-press-topdown-v2: push the button down from above
def button_press_topdown_v2(robot):
    # Steps:
    #  1. Put gripper vertically aligned with button
    #  2. Move gripper down on button
    #  3. Move gripper