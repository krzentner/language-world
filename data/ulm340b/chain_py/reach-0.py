
    # Steps:
    #  1. Move the gripper to the target location
    # We can move the robot's gripper straight to the goal.
    if check("the robot's gripper is not at goal"):
        robot.move("gripper to goal")

# button-press-side: press down the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put the gripper vertically aligned with the button
    #  2. Line up the gripper with the button as seen from the side
    #  3. Push the gripper against the button
    # The button is small, so it's important to make sure the gripper is
    # vertically aligned with it before pressing.
    if check("the robot's gripper is not vertically aligned with the button and the button is not above the robot's gripper"):
        robot.move("gripper vertically aligned with button")
    # If the gripper is vertically aligned, now we need to move the gripper into
    # the button as seen from the side.
    # We do this by aligning the robot's gripper with the button as seen from the
    # front.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper to button")
    # Once the robot's gripper is horizontally and vertically aligned with the
    # button as seen from the side, push the gripper into the button.
    if check("the robot's gripper is horizontally aligned with button and the robot's gripper is vertically aligned with button"):
        robot.push("the gripper into the button")

# button-press-topdown-side: push the button down from the top or from the
# side, whichever works best
def button_press_topdown_side(robot):
    # Steps:
    #  1. If the button is right of the gripper, move the gripper to the left
    #     of the button to try to press from the side
    #  2. If the gripper is above the button, try to press down on it from the
    #     top
    #  3. If the button is to the right of the gripper, but not vertically
    #     aligned, move the gripper vertically aligned above the