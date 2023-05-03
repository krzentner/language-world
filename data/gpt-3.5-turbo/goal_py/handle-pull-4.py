# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper below handle
    #  2. Move gripper up around the handle
    #  3. Pull up on the handle
    # First, put the gripper mostly below the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # As long as the gripper is almost below the handle, closing it should line it up
    # all the way below the handle.
    if check("the robot's gripper is below the handle and the robot's gripper is closed"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, we can pull up on the handle.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle")