

Steps:
1. Put gripper beside the handle
2. Push down on the handle from the side

# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper beside the handle
    #  2. Push down on the handle from the side
    # First, move the gripper to the side of the handle.
    if check("the robot's gripper is not beside the handle"):
        robot.move_gripper("beside the handle")
    # Once the gripper is beside the handle, we can push down on it from the side.
    if check("the robot's gripper is beside the handle"):
        robot.move_gripper("vertically aligned with the handle")