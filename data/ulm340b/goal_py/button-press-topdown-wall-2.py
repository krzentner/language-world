
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move the gripper over the short wall
    #  3. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Because this is "wall", the gripper isn't vertically aligned.
    # Move the gripper over the wall.
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.move_gripper("above the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push in on the button from the side
    # Because this is "side", we just need to line up the gripper from in front.
    # Line up the robot's gripper from in front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button")
    # Now that the gripper is lined up, just push the button from the side.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)

# button-press-side-wall: push the button down from the side with a short wall in the way
def button_press_side_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Move the gripper over the short wall
    #  3. Push in on the button from the side
    # Because this is "side", we just need to line up the grip