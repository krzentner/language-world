# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper to the right of the handle
    #  2. Grab the handle with the gripper
    #  3. Lift the handle upwards
    # First, move the gripper near to the handle
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near the handle")
    # If the gripper is near the handle, grab it
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.grab("the handle with the gripper")
    # If the gripper has a hold of the handle, lift it upwards
    if check("the robot's gripper is holding the handle"):
        robot.lift("the handle upwards")