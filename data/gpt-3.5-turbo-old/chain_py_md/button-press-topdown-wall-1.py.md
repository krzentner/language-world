# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top while avoiding the wall using a zig-zag pattern
    # If the robot's gripper is not vertically lined up with the button,
    # line up the gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # If there's a wall blocking the path to the button,
    # move down and to the right of the button, then up and to the left,
    # and continue zig-zagging until we can push down on the button.
    # Move the gripper down and to the right.
    if check("there is a wall blocking the path to the button and the robot's gripper is not close enough"):
        robot.move("down and right")
    # Move the gripper up and to the left.
    elif check("there is a wall blocking the path to the button and the robot's gripper is not close enough"):
        robot.move("up and left")
    # Once we're close enough and the gripper is lined up with the button, 
    # push down to press the button.
    elif check("the robot's gripper is vertically aligned with button and the robot's gripper is close enough"):
        robot.push("down on button")