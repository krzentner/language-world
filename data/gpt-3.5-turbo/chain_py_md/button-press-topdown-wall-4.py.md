# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Check if there's a wall in the way
    #  3. Move gripper over the wall
    #  4. Push down on the button from the top
    # First, line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Check if there's a wall in the way, by checking if the button is not below
    # the gripper.
    if check("the button is not below the robot's gripper"):
        # If there's a wall, move the gripper to the right of the wall.
        robot.move("gripper over wall")
    # Now that the gripper is lined up and the wall isn't in the way, just push
    # down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")