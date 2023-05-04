

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper with the button from the front
    #  2. Move the robot's gripper around the wall
    #  3. Push the button
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper above button")
    # If the gripper is horizontally aligned with the button from the front, we
    # can move to pushing the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button")

# button-press-angled: push the button from an angle with a short wall in the way
def button_press_angled(robot):
    # Steps:
    #  1. Line up the gripper with the button from the front
    #  2. Move the robot's gripper around the wall
    #  3. Push the button
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper above button")
    # If the gripper is horizontally aligned with the button from the front, we
    # can move to pushing the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button")


# button-press-side: push the button from the side with a short wall in the way
def button_press_side(robot):
    # Steps:
   