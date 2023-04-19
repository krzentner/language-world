# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper next to the handle
    #  2. Press down on the handle
    # First, put the gripper next to the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper to side of handle")
    # Then, press down on the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.press("down on handle from the side")