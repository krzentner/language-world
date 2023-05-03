# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Move gripper above the handle
    #  2. Hook the gripper beneath the handle and lift it up
    # First, move the gripper roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is not hooked beneath the handle and open, move it down and hook it.
    if check("the robot's gripper is not hooked beneath the handle and the robot's gripper is open"):
        robot.move_gripper("below the handle", close_gripper=True)
    # If the gripper is hooked beneath the handle and closed, lift the handle up.
    if check("the robot's gripper is hooked beneath the handle and the robot's gripper is closed"):
        robot.move_gripper("above the handle and slightly pulled up")