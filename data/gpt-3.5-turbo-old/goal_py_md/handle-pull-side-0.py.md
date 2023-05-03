# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper to the right of the handle
    #  2. Drop gripper around handle
    #  3. Lift gripper while holding the handle until it's in the "up" position
    # First, put the gripper to the right of the handle
    if check("the robot's gripper is not right of the handle"):
        robot.move_gripper("right of the handle")
    # If the gripper is right of the handle, drop the gripper around it
    if check("the robot's gripper is right of the handle and the robot's gripper is not around the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("around the handle")
    # If the gripper is around the handle, lift the gripper while holding the handle to pull it up
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")