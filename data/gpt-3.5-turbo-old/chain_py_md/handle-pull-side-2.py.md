# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put the gripper to the left of the handle
    #  2. Move the gripper to the handle
    #  3. Turn the gripper to wrap around the handle
    #  4. Pull up the handle
    # Move the gripper to the left of the handle.
    if check("the robot's gripper is not to the left of the handle"):
        robot.move("gripper to the left of the handle")
    # Move the gripper to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to the handle")
    # Turn the gripper to wrap around the handle.
    if check("the robot's gripper is not wrapped around the handle"):
        robot.wrap("gripper around the handle")
    # Pull up the handle.
    if check("the robot's gripper is wrapped around the handle"):
        robot.pull("the handle up")