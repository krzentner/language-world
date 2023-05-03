# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper next to the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle
    # First, put the gripper next to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper next to handle")
    # If the gripper is next to the handle, grab it with the gripper.
    if check("the robot's gripper is near the handle and the gripper is open"):
        robot.grab("handle")
    # Once the gripper has the handle in its grasp, pull it up.
    if check("the robot's gripper is holding the handle"):
        robot.pull("handle up")