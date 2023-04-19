

# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put the robot's gripper in front of the button and the wall
    #  2. Push against the wall to push the button
    #  3. Push harder against the wall to press the button
    # First, move the robot's gripper to the same level as the button and the
    # wall. We need the wall to be between the button and the gripper so that we
    # can press the button.
    if check("the robot's gripper is not in front of button and wall"):
        robot.put("gripper in front of button and wall")
    # Once the gripper is in front of the button and wall, push the wall slightly
    # forward to press the button.
    if check("the robot's gripper is in front of button and wall"):
        robot.push("against wall")
    # If the button hasn't been pressed yet, push harder against the wall.
    if check("the button is not pressed"):
        robot.push("harder against wall")