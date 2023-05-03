# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper below the handle
    #  2. Grab the handle with the gripper
    #  3. Pull upward on the handle
    #  4. Release the handle
    # First, put the gripper below the handle.
    if check("the robot's gripper is not below the handle"):
        robot.move("gripper to below handle")
    # Once the gripper is below the handle, grab the handle.
    if check("the robot's gripper is below the handle and the robot's gripper is open"):
        robot.grab("handle")
    # Pull upward on the handle while it is grabbed by the gripper.
    if check("the robot's gripper has grabbed the handle and the handle is not above the robot's gripper"):
        robot.pull("handle upward")
    # Release the handle from the gripper.
    if check("the robot's gripper is holding the handle and the handle is above the robot's gripper"):
        robot.release("handle")