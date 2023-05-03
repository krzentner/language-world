# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move gripper near button
    #  2. Move gripper up above the wall
    #  3. Align gripper with button
    #  4. Push down on button
    # If the robot's gripper is not near the button, move it near the button.
    if check("the robot's gripper is not near button"):
        robot.move("gripper near button")
    # If the robot's gripper is below the wall, move it up above the wall.
    if check("the robot's gripper is below the wall"):
        robot.move("gripper up above the wall")
    # If the robot's gripper is not vertically aligned with the button, align it.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.align("gripper with button")
    # Push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")