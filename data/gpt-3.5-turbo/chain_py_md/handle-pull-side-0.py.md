# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper next to the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # Put the gripper next to the handle.
    if check("the robot's gripper is not next to the handle"):
        robot.move("gripper to the side of the handle")
    # Once the gripper is near the handle, grab the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.grab("the handle")
    # If the gripper is around the handle, pull up on the handle.
    if check("the robot's gripper is around the handle"):
        robot.pull("up on the handle")