# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    # 1. Check if there is a short wall in the way
    # 2. If there is a wall, move the gripper left of the wall
    # 3. Line up the gripper as viewed from above with the button
    # 4. Push down on the button from the top
    # First, check if there is a wall in the way.
    if check("there is a wall between the robot's gripper and the button"):
        robot.move_gripper("left of the wall")
    # Once the gripper is left of the wall, line it up from above with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")