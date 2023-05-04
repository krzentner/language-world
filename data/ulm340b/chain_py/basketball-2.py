
    # Steps:
    #  1. Hold the ball up in the air
    #  2. Put the ball in the hoop
    # Start with picking up the ball.
    # First, put the gripper above ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above ball")
    # If the gripper is above the ball but not around it, move the gripper around
    # the ball.
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is not around ball"):
        robot.put("gripper around ball")
    # If the gripper is around the ball, pick up the ball.
    if check("the robot's gripper is around ball and the robot's gripper is open"):
        robot.grab("ball")
    # If the ball is below the robot's gripper, we picked up the ball!
    # Now try to put it into the hoop.
    if check("ball is below the robot's gripper"):
        robot.put("the ball into the hoop")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper horizontally
    #  2. Push down on the button from the side
    # Because this is "side", we just need to line up the gripper horizontally.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper horizontal with button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")

# button-press-topdown-side: push the button down from above
def button_press_topdown_side(robot):
    # Steps:
    #  1. Line up the gripper in front of the button
    #  2. Push down on the button from the side
    #  3. Put the gripper vertically aligned with button
    #  4. Push down on the button from the side
    #  5. Put the gripper