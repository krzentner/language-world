
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Lift up the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # As long as the gripper is lined up with the handle from the front, we can
    # just lift up the handle to solve the task.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("almost vertically aligned with the handle")

# handle-pull-up: pull up the handle from above
def handle_pull_up(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Lift up the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is still mostly below the gripper and the gripper isn't
    # around the handle, grab the handle.
    if check("the handle is not almost vertically aligned with the robot's gripper and the robot's gripper is not around the handle"):
        robot.move_gripper("near the handle")
    # Now that the gripper is around the handle, we can just pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("almost vertically aligned with the handle")

# latch-pull: pull up the latch
def latch_pull(robot):
    # Steps:
    #  1. Put gripper above latch
    #  2. Grab the latch with the gripper
    #  3. Lift up the latch
 