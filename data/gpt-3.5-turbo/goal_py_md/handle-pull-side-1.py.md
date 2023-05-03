# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Position the gripper to the side of the handle
    #  2. Place the gripper around the handle
    #  3. Pull the handle up
    # First, position the gripper to the side of the handle.
    if check("the robot's gripper is not beside the handle"):
        robot.move_gripper("beside the handle")
    # Once the gripper is beside the handle, place it around the handle.
    if check("the robot's gripper is beside the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Finally, pull the handle up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle", close_gripper=True)