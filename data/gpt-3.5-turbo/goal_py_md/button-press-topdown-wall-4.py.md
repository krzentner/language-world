# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move the gripper up and over the wall
    #  3. Push down on the button from the top
    # Because there is a wall in the way, the gripper needs to move up and over
    # the wall to be able to push the button downwards.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Move the gripper over the wall and angle it down towards the button.
    if check("the robot's gripper is vertically aligned with button and is on the wrong side of the wall"):
        robot.move_gripper("over the wall and angled down towards the button")
    # Now that the gripper is lined up and angled correctly, just push down on the button.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("pushing down on the button")