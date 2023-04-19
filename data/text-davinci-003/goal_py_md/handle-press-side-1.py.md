

# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Push gripper sideways against handle 
    #  3. Push handle down
    # Put the gripper roughly aligned above the handle.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # With the gripper still aligned, move the gripper to the side of the handle.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not close to handle"):
        robot.move_gripper("close to handle")
    # Now the gripper should be position correctly to push the handle down.
    if check("the robot's gripper is close to handle"):
        robot.move_gripper("below the handle")