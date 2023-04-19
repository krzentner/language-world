
    # Steps:
    #  1. Move gripper towards button
    #  2. Push against wall
    #  3. Push down on button from top
    # If the gripper is not near the button, move it to the button.
    if check("the robot's gripper is not near the button"):
        robot.move("gripper to button")
    # If the gripper touches the wall, push against the wall in order to move the
    # wall further away from the button.
    # If the button is close enough to the wall, this push should move the wall
    # enough to line up the gripper vertically with the button.
    if check("the robot's gripper is touching wall"):
        robot.push("wall")
    # If the gripper is almost lined up with the button, push down on the
    # button.
    if check("the robot's gripper is almost vertically aligned with button"):
        robot.push("down on button")
    # If the gripper is not lined up with the button and the robot's gripper
    # is not touching the wall, move the robot's gripper to the button and
    # repeat the previous steps.