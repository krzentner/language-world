
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("above the wall")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# button-press-side: push the button sideway
def button_press_side(robot):
    # Steps:
    #  1. Move the gripper around the button
    #  2. Push the button from the side
    # We only need to get the gripper around the button to press it from the
    # side.
    if check("the robot's gripper is not around button"):
        robot.move_gripper("around the button", close_gripper=True)
    # Now push the button from the side.
    if check("the robot's gripper is around the button"):
        robot.move_gripper("near the button")

# button-press-side-wall: push the button sideway with a short wall in the way
def button_press_side_wall(robot):
    # Steps:
    #  1. Move the gripper around the button
    #  2. Push the button from the side
    # We only need to get the gripper around the button to press it from the
    # side.
    if check("the robot's gripper is not around button"):
        robot.move_gripper("above the wall")
    # Now push the button from the side.
    if check("the robot's gripper is around the button"):
        robot.move_gripper("near the button")

# cloth-cover: cover the goal location with the cloth
def cloth_cover(robot):
    # Steps:
    #  1. Put gripper above the cloth
    #  2. Grab cloth with the gripper
    #  3. Pull the cloth to the goal location
  