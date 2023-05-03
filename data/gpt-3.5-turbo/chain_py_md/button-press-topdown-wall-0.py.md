# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move gripper to above the button
    #  2. Move gripper forward until it hits the wall
    #  3. Move gripper slightly to the side of the button
    #  4. Push down on the button from the top
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Move the gripper forward until it hits the wall.
    if check("the gripper is not touching the wall"):
        robot.move("gripper forward until it hits the wall")
    # Move the gripper slightly to the side of the button.
    if check("the robot's gripper is not slightly to the side of the button"):
        robot.move("gripper slightly to the side of the button")
    # Finally, push down on the button from the top.
    if check("the robot's gripper is aligned with the button"):
        robot.push("down on button")