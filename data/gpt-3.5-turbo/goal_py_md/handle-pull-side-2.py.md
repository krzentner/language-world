# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper on side of the handle
    #  2. Move gripper around the handle from the side
    #  3. Grab the handle
    #  4. Pull up the handle
    # If the handle is not on the side of the gripper, move the gripper to the side of the handle.
    if check("the handle is not on the side of the robot's gripper"):
        robot.move_gripper("on the side of the handle")
    # If the handle is on the side of the gripper but the gripper is not around the handle, move the
    # gripper around the handle from the side.
    if check("the robot's gripper is not around the handle and is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
        robot.move_gripper("around the handle from the side")
    # If the gripper is around the handle, grab the handle.
    if check("the robot's gripper is around the handle and the gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the handle is grabbed, pull up the handle.
    if check("the robot's gripper is around the handle and the gripper is closed"):
        robot.move_gripper("above the handle")