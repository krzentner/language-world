# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Check if there's a wall between the gripper and button
    #  3. Move around the wall if it exists
    #  4. Push down on the button from the top
    # Put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Check if there's a wall between the gripper and the button.
    if check("there is a short wall between the gripper and the button"):
        # Move around the wall to get to the button.
        robot.move("around the wall")
    # Once there's no wall between the gripper and the button, push down on the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.push("down on button")