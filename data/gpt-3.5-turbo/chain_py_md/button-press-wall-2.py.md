# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put gripper near the button and aligned with it
    #  2. Move gripper forward until it contacts the wall
    #  3. Slide the gripper along the wall until it's above the button
    #  4. Push down on the button
    # First, align the gripper with the button
    if check("the robot's gripper is not aligned with the button and is not positioned nearby"):
        robot.place("gripper near button and aligned")
    # Move gripper forward toward the wall
    if check("the robot's gripper is not contacting the wall"):
        robot.move("gripper forward until it contacts the wall")
    # Slide the gripper along the wall toward the button
    if check("the gripper is not above the button"):
        robot.slide("gripper along the wall until it's above the button")
    # Push down on the button
    if check("the gripper is above the button and not pushed down"):
        robot.push("down on the button")