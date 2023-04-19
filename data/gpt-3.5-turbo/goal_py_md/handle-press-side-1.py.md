# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    # 1. Put gripper above handle
    # 2. Grab the handle with the gripper
    # 3. Rotate the gripper 90 degrees to the left
    # 4. Push the handle down
    # First, put the gripper above the handle
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is not between the fingers of the gripper, grab it
    if check("the handle is not between the fingers of the gripper"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Rotate the gripper 90 degrees to the left
    if check("the gripper is not rotated 90 degrees to the left"):
        robot.rotate_gripper("90 degrees to the left")
    # Push the handle down
    if check("the gripper is rotated 90 degrees to the left"):
        robot.move_gripper("near the table")