
    # Steps:
    #  1. Put the gripper above the ball
    #  2. Drop gripper around the ball
    #  3. Put the ball above the hoop
    #  4. Drop the ball into the hoop
    # If the gripper isn't above the ball, put it above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball", close_gripper=True)
    # If the ball is not in the gripper, put the gripper around the ball.
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.move_gripper("above the ball")
    # If the gripper is around the ball and it's open, maybe we can grab it.
    if check("the robot's gripper is around the ball and the robot's gripper is closed"):
        robot.move_gripper("above the hoop")
    # If the ball is in the hoop, let go of the ball.
    if check("the robot's gripper is around the ball and the robot's gripper is closed"):
        robot.move_gripper("above the robot's gripper")

# button-press-side: push the button with the gripper
def button_press_side(robot):
    # Steps:
    #  1. Put the gripper left of the button
    #  2. Push the button
    # First, put the gripper left of the button.
    if check("the robot's gripper is not left of the button"):
        robot.move_gripper("left of the button")
    # Once the gripper is left of the button, push it.
    if check("the button is in front of the robot's gripper"):
        robot.move_gripper("almost horizontally aligned with the button")

# peg-insert-topdown: put the peg above the hole and drop it in
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put the gripper above the peg
    #  2. Put the peg above the hole
    #  3. Drop the peg
    # If the gripper is not around the peg, put it above the peg.
    if