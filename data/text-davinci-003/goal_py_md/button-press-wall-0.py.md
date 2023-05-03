

# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Follow short wall at angle to press button
    #  3. Push button through the wall
    # First, we need to move the robot's gripper to the left of the button.
    # The angle of the wall may make this a bit tricky.
    if check("the robot's gripper is not to the left of the wall"):
        robot.move_gripper("below the wall at an angle")
    # Now that the gripper is on the left of the wall, we can move it slowly at
    # an angle towards the button.
    if check("the robot's gripper is below the wall at an angle and the robot's gripper is not near the button"):
        robot.move_gripper("below the wall at an angle", close_gripper=True)
    # If the gripper is nearly lined up with the button, push the button through
    # the wall and follow it until it is pressed all the way.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("forward aligned with the button")