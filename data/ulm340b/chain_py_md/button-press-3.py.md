

This will push the button in the same environment as the button-press-topdown program, but will use the robot's gripper to push the button from the front.


Steps:
  1. Line up the gripper as viewed from in front
  2. Push down on the button from in front

""",

"""

# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push down on the button from in front
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")
""",

"""

# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push down on the button from in front
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")

# press-side: push the button from the side
def press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the button from the side
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper above button")
    # Now