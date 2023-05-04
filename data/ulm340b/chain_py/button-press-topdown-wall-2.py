
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

# button-press-left: push the button left from the side
def button_press_left(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the button left
    # Because this is not "topdown", we just need to line up the gripper on the
    # side.
    # Line up the robot's gripper horizontally.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper left of button")
    # Now that the gripper is lined up, just push the button left.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button left")

# button-press-left-wall: push the button left from the side with a short wall in the way
def button_press_left_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the button left
    # Because this is not "topdown", we just need to line up the gripper on the
    # side.
    # Line up the robot's gripper horizontally.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper left of button")
    # Now that the gripper is lined up, just push the button left.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("button left")

# button-press-left-side: push the button left from the side
def button_press_left_side(robot):
    # Steps:
  