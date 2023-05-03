# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper next to handle
    #  2. Grab handle with gripper
    #  3. Pull up on handle
    # First, put the gripper next to the handle so that we can grab it without pushing it first.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the gripper is near the handle, open the gripper and insert it around the handle.
    # We want to make sure we have a good grip on the handle before pulling up on it.
    if check("the robot's gripper is near the handle and the gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, pull up on it.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")