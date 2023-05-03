# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put the gripper next to the handle
    #  2. Grab the handle
    #  3. Pull up on the handle
    # If the gripper is not next to the handle, put the gripper next to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper next to handle")
    # If the gripper is near the handle but not around it, grab the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    # If the gripper is around the handle, pull up on the handle.
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle")