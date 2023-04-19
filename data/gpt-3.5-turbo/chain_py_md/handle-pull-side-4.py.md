# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put the gripper level with the handle
    #  2. Hook the gripper around the handle
    #  3. Pull the handle up
    # First, put the gripper level with the handle.
    if check("the robot's gripper is not level with the handle"):
        robot.put("gripper level with handle")
    # Next, hook the gripper around the handle.
    if check("the robot's gripper is level with handle and the gripper is not hooked around the handle"):
        robot.hook("gripper around handle")
    # Finally, pull the handle up.
    if check("the gripper is hooked around the handle"):
        robot.pull("handle up")