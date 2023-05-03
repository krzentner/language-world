# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Push gripper down on handle
    #  3. Push handle down further
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is above the handle, we can push down on it to activate it.
    if check("the robot's gripper is above the handle and the robot's gripper is not pushing down on the handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the robot's gripper is already pushing down on the handle, push it
    # down further to activate it.
    if check("the robot's gripper is pushing down on the handle"):
        robot.move_gripper("on top of the handle")