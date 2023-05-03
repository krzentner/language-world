# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Put the gripper above the button
    #  2. Move the gripper forward until it hits the wall
    #  3. Move the gripper up slightly
    #  4. Move the gripper forward into the button
    # If the gripper is not vertically lined up with the button, put it above
    # the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Move the gripper forward until it hits the wall.
    while check("the robot's gripper is not against wall"):
        robot.move("gripper forward")
    # Move the gripper up slightly so that it clears the wall.
    robot.move("gripper up slightly")
    # Move the gripper forward into the button.
    robot.move("gripper forward")