# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #   1. Line up the gripper as viewed from above
    #   2. Move the gripper above the wall
    #   3. Move the gripper to the button
    #   4. Push down on the button from the top
    # First, line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # If there is a wall in the way, move the gripper above the wall
    if check("there is a short wall between the robot's gripper and the button"):
        robot.move("gripper above the wall")
    # If the gripper is above the wall, move it to the button
    if check("the robot's gripper is above the wall and not vertically aligned with the button"):
        robot.move("gripper to button")
    # Push down on the button
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")