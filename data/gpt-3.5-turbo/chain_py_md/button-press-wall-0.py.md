# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put gripper in front of the button and the wall
    #  2. Move gripper forward to push the button
    # The wall obstructs the line of sight of the robot's gripper, so we have to
    # push the button from the front instead.
    # We need to make sure the gripper is aligned with the button despite the
    # wall obstructing the view.
    if check("the robot's gripper is not horizontally aligned with the button and wall"):
        robot.put("gripper in front of the button and the wall")
    # Now that the gripper is roughly aligned with the button, move it forward
    # to push the button.
    if check("the robot's gripper is horizontally aligned with the button and wall"):
        robot.push("forward to push the button")