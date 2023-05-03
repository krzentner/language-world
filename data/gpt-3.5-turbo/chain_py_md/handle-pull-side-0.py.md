# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Grab the handle
    #  3. Pull the handle up
    # This task is similar to `peg_insert_side` in terms of the robot's
    # approach to the handle.
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    # If the gripper is not around the handle, grab it.
    if check("the robot's gripper is not around the handle"):
        robot.grab("the handle")
    # Once the gripper is around the handle, pull up on the handle.
    if check("the robot's gripper is around the handle"):
        robot.pull("the handle up")