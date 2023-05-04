
    # Steps:
    #  1. Line up the gripper from in front of the button
    #  2. Push the button
    # First, line up the gripper.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper to button")
    # Now push the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button")

# button-press-side: push the button from the front with a tall wall in the way
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper from the front of the button
    #  2. Push the button from the side
    # First, line up the gripper from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper to button")
    # Now push the button from the side.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button sideways")

# button-press-top: push the button from the top
def button_press_top(robot):
    # Steps:
    #  1. Line up the gripper from in front of the button
    #  2. Move the gripper above the button
    #  3. Push the button from the top
    # First, line up the gripper from in front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper to button")
    # Now line up the gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that we're lined up from above, push the button from the top.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("button from top")

# button-press-wall-top: push the button from the top, over a short wall
def button_press_wall_top(robot):
    # Steps:
    #  1. Line up the gripper from in front of the button
    #  2. Move the gripper above the button
    #  3