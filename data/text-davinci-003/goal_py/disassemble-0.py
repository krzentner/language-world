
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Align the gripper with the wrench as seen from above
    #  3. Grab the wrench with the gripper
    #  4. Pull the wrench off the peg   
    # First, make sure the gripper is above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench is lined up on top, lower the gripper and grab it.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.move_gripper("left of the peg", close_gripper=True)

# button-press-side: press the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Align the gripper with the button as seen from the side
    #  3. Push the button with the gripper
    # First, make sure the gripper is left of the button.
    if check("the robot's gripper is not left of the button"):
        robot.move_gripper("left of the button")
    # If the gripper is left of the button, we should be able to line it up by
    # lowering it.
    # Since we don't need to grab the button, we don't need to close the
    # gripper.
    if check("the robot's gripper is left of the button and the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button")
    # Once the gripper is lined up with the button, we can just press it.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")