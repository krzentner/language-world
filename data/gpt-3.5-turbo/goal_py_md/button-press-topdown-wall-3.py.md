# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move the gripper to the wall where the button is located
    #  3. Move the gripper above the button
    #  4. Push down on the button from the top
    # The distance to the wall is unknown, so we will have to move the gripper
    # until it has located the wall.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Move the gripper towards the wall until it stops.
    if check("the robot's gripper is not touching the wall"):
        robot.move_gripper("to the wall with the button")
    # Once we have located the wall, move the gripper to above the button.
    if check("the robot's gripper is touching the wall and is not above the button"):
        robot.move_gripper("above the button on the wall", close_gripper=True)
    # Now that the gripper is above the button, just push down on the button.
    if check("the robot's gripper is above the button on the wall and the robot's gripper is closed"):
        robot.move_gripper("near the button on the wall")