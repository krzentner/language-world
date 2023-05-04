
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the button from the front
    # Line up the robot's gripper.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")

# button-press-topdown-wall: push the button from the top with a wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the top
    #  2. Push down on the button from the top
    # Line up the robot's gripper.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# switch-press-topdown: push the switch from above
def switch_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the switch to the side from above
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.move_gripper("vertically aligned with the switch", close_gripper=True)
    # Now that the gripper is lined up, push the switch to the side.
    if check("the robot's gripper is vertically aligned with switch"):
        robot.move_gripper("horizontally aligned with switch")

# switch-press-topdown-side: push the switch to the side from above
def switch_press_topdown_side(robot):
    # Steps:
    # 