# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Move the gripper to the left of the wall
    #  2. Move the gripper to the front of the wall
    #  3. Move the gripper down to the button
    #  4. Push down on the button
    # We need to move the gripper to the left of the wall to start. If the gripper
    # is not to the left of the wall, move it there.
    if check("the robot's gripper is not to the left of the wall"):
        robot.move("gripper to left of wall")
    # Once the gripper is left of the wall, move it to the front of the wall. If
    # the gripper is not in front of the wall, move it there.
    if check("the robot's gripper is not in front of the wall"):
        robot.move("gripper to front of wall")
    # Now that the gripper is in front of the wall, move it down to the button.
    if check("the robot's gripper is not near the button"):
        robot.move("gripper to button")
    # Once the gripper is near the button, push down on it to press the button.
    if check("the robot's gripper is near the button"):
        robot.push("down on button")