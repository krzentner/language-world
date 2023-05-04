
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around handle
    #  3. Pull handle up
    # First, put the gripper almost above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the handle")
    # If the gripper is roughly lined up with the handle, but it's not already
    # around the handle, move it around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is lined up with the handle from in front and around it,
    # we can pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("in front of the handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up gripper as viewed from the side
    #  2. Push down on the button from the side
    # Line up the robot's gripper from the side with the button.
    if check("the robot's gripper is not side aligned with the button"):
        robot.move_gripper("side aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is side aligned with the button"):
        robot.move_gripper("vertically aligned with the button")

# handle-pull-front: pull up the handle from the front
def handle_pull_front(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull handle up
    # First, put the gripper above the handle.
    if check("the