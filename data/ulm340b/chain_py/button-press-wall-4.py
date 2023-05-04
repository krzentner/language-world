
    # Steps:
    #  1. Place gripper roughly to left of button
    #  2. Insert gripper around front of button
    #  3. Push button
    # Because we have to push from the side, we should first line up the gripper
    # from above.
    if check("the robot's gripper is not to the left of button and the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    # Insert the gripper to the right of the button
    if check("the robot's gripper is to the left of button"):
        robot.insert("gripper around front of button")
    # Now push the button
    if check("the robot's gripper is horizontally aligned with button and the robot's gripper is right of button"):
        robot.push("button")

# button-press-long: push the button from the front with a long wall in the way
def button_press_long(robot):
    # Steps:
    #  1. Place gripper above and in front of button
    #  2. Push down and to the side on the button
    # Because we have to push from the side, we should first line up the gripper
    # from above.
    if check("the robot's gripper is not above button and the robot's gripper is not vertically aligned with button"):
        robot.place("gripper above button")
    # Push the button by moving the gripper down and to the side.
    if check("the robot's gripper is above button and the robot's gripper is not horizontally aligned with button"):
        robot.push("down and to the side")

# button-press-topdown-long: push the button down from above with a wall in the way
def button_press_topdown_long(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above and to the side
    #  2. Push down on the button from the top
    # Because we have to push from the side, we should first line up the gripper
    # from above.
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not above button"):
        robot.put("gripper above button")
    # Push the button by moving