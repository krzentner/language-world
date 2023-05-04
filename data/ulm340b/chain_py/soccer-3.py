
    # Steps:
    #  1. Put the gripper behind the ball
    #  2. Push the ball to the goal
    # Put the robot's gripper behind the ball, to push it.
    if check("the robot's gripper is not behind the ball"):
        robot.put("the gripper behind the ball")
    # As long as the robot's gripper is behind the ball, we can push the ball to
    # the goal.
    if check("the robot's gripper is behind the ball"):
        robot.push("the ball towards the goal")

# button-press-topdown-side: push the button down from above and to the side
def button_press_topdown_side(robot):
    # Steps:
    #  1. Put the gripper above and to the side of the button
    #  2. Put the gripper to the side of the button
    #  3. Push the button down
    # To push the button down from the side, put the robot's gripper above the
    # button and to the side.
    if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is not horizontally aligned with the button"):
        robot.put("the gripper above and to the side of the button")
    # After that, put the gripper to the side of the button.
    # Since the gripper is still above the button, it should move down onto the
    # button while moving to the side.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not horizontally aligned with the button"):
        robot.put("the gripper to the side of the button")
    # If the gripper is on the side of the button, push the button down.
    if check("the robot's gripper is horizontally aligned with the button"):
        robot.push("the button down")

# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Drop gripper to the side of the button
    #  3. Push the button down
    # The robot's gripper is not vertically aligned with the button, so put it
    #